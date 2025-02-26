from typing import Literal
import os
import getpass

from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import END, START, StateGraph, MessagesState 
from langgraph.prebuilt import ToolNode
from langgraph.types import Command 

os.environ["LANGSMITH_TRACING"] = "true"
if not os.environ.get("LANGSMITH_API_KEY"):
  os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter API key for Langsmith: ")
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

@tool
def search(query: str):
    """Call to surt the web."""
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny"

tools = [search]
tool_node = ToolNode(tools)

model = ChatOpenAI(model="gpt-4", temperature=0).bind_tools(tools)

def call_model(state: MessagesState) -> Command[Literal['tools', END]]:
    messages = state['messages']
    response = model.invoke(messages)
    if len(response.tool_calls) > 0:
        next_node = "tools"
    else:
        next_node = END
    return Command(goto=next_node, update={"messages": [response]})

workflow = StateGraph(MessagesState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge(START, "agent")
workflow.add_edge("tools", "agent")
app = workflow.compile()

# response = app.invoke(
#     {"messages": [{"role": "user", "content": "What is the weather in sf"}]},
#     debug=True
# )

def transfer_to_weather_agent():
    """Call this to transfer to the weather agent."""

tools = [transfer_to_weather_agent]
main_model = ChatOpenAI(model="gpt-4", temperature=0).bind_tools(tools)

def call_main_model(state: MessagesState) -> Command[Literal['weather_agent', END]]:
    messages = state['messages']
    response = main_model.invoke(messages)
    if len(response.tool_calls) > 0:
        return Command(goto="weather_agent")
    else:
        return Command(goto=END, update={"messages": [response]})
    
workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_main_model)
workflow.add_node("weather_agent", app)
workflow.add_edge(START, "agent")
multi_agent = workflow.compile()

response = multi_agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in sf"}]},
    debug=True
)

