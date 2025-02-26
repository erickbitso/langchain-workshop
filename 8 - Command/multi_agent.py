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

############
@tool
def respond_questions(input: str):
    """Call to answer questions to internal knowledge base."""
    return f"In order to do that, you should use Komodor"

knowlege_tools = [respond_questions]
knowledge_tool_node = ToolNode(knowlege_tools)

knowledge_model = ChatOpenAI(model="gpt-4", temperature=0).bind_tools(knowlege_tools)

def knowledge_LLM_Node(state: MessagesState) -> Command[Literal['tools', END]]:
    messages = state['messages']
    prompt = "You must always use the available tool respond_questions to respond to questions"
    temp_messages = messages.copy()
    temp_messages.append({"role": "system", "content": prompt})
    response = knowledge_model.invoke(temp_messages)  # Use temp_messages with the prompt
    if len(response.tool_calls) > 0:
        next_node = "tools"
    else:
        next_node = END
    return Command(goto=next_node, update={"messages": [response]})

knowledge_workflow = StateGraph(MessagesState)

knowledge_workflow.add_node("agent", knowledge_LLM_Node)
knowledge_workflow.add_node("tools", knowledge_tool_node)
knowledge_workflow.add_edge(START, "agent")
knowledge_workflow.add_edge("tools", END)  # Modified line
knowledge_agent = knowledge_workflow.compile()

# response = knowledge_agent.invoke(
#     {"messages": [{"role": "user", "content": "How do I restart the webhead service?"}]},
#     debug=True
# )

# os._exit(0)

############

@tool
def get_service_health(service_name: str, environment: str = "production"):
    """Call to get the state or health of a service."""
    return f"Service: {service_name} in {environment} is in a healthy state"

@tool
def restart_service(service_name: str, environment: str = "production"):
    """Call to restart a service."""
    return f"Service: {service_name} in {environment} has been restarted"

SRE_tools = [get_service_health,restart_service]
SRE_tool_node = ToolNode(SRE_tools)

SRE_model = ChatOpenAI(model="gpt-4", temperature=0).bind_tools(SRE_tools)

def SRE_LLM_Node(state: MessagesState) -> Command[Literal['tools', END]]:
    messages = state['messages']
    response = SRE_model.invoke(messages)
    if len(response.tool_calls) > 0:
        next_node = "tools"
    else:
        next_node = END
    return Command(goto=next_node, update={"messages": [response]})

sre_workflow = StateGraph(MessagesState)

sre_workflow.add_node("agent", SRE_LLM_Node)
sre_workflow.add_node("tools", SRE_tool_node)
sre_workflow.add_edge(START, "agent")
sre_workflow.add_edge("tools", "agent")
SRE_agent = sre_workflow.compile()

# response = SRE_agent.invoke(
#     {"messages": [{"role": "user", "content": "What's the health of motorsito service?"}]},
#     debug=True
# )

# response = SRE_agent.invoke(
#     {"messages": [{"role": "user", "content": "Restart webhead service."}]},
#     debug=True
# )

############

# os._exit(0)

# Add knowledge agent transfer tool
def transfer_to_sre_agent():
    """Call this to transfer to the SRE agent."""

def transfer_to_knowledge_agent():
    """Call this to transfer to the knowledge agent."""

# Update tools list for main model
tools = [transfer_to_sre_agent, transfer_to_knowledge_agent]
main_model = ChatOpenAI(model="gpt-4", temperature=0).bind_tools(tools)

# Fix the main_llm_node function
def main_llm_node(state: MessagesState) -> Command[Literal['sre_agent', 'knowledge_agent', END]]:
    messages = state['messages'].copy()  # Make a copy to avoid modifying the original
    # Define the prompt for this node
    prompt = (
        "You are a Platform support agent.\n"
        "If the user's message is a question about HOW TO do something, includes 'how do I', or asks about procedures/documentation/internal knowledge, use transfer_to_knowledge_agent.\n"
        "If the user's message is a direct request to check health, get status, or perform an action on a specific service (like 'restart webhead' or 'check status of motorsito'), use transfer_to_sre_agent.\n"
        "Questions that start with 'How do I...' should always go to the knowledge agent, even if they mention services.\n"
        "Ensure to accurately distinguish between knowledge questions and action requests."
    )
    temp_messages = messages.copy()
    temp_messages.append({"role": "system", "content": prompt})
    response = main_model.invoke(temp_messages)
    
    # Check which tool was called
    if len(response.tool_calls) > 0:
        tool_name = response.tool_calls[0]["name"]
        if tool_name == "transfer_to_sre_agent":
            return Command(goto="sre_agent")
        elif tool_name == "transfer_to_knowledge_agent":
            return Command(goto="knowledge_agent")
    
    # Default case
    return Command(goto=END, update={"messages": [response]})

    
main_workflow = StateGraph(MessagesState)
main_workflow.add_node("main_agent", main_llm_node)
main_workflow.add_node("sre_agent", SRE_agent)
main_workflow.add_node("knowledge_agent", knowledge_agent)
main_workflow.add_edge(START, "main_agent")
multi_agent = main_workflow.compile()

# response = multi_agent.invoke(
#     {"messages": [{"role": "user", "content": "What is the state of the motorsito service?"}]},
#     debug=True
# )

# response = multi_agent.invoke(
#     {"messages": [{"role": "user", "content": "Restart the webhead service."}]},
#     debug=True
# )

response = multi_agent.invoke(
    {"messages": [{"role": "user", "content": "How do I restart a service?"}]},
    debug=True
)

