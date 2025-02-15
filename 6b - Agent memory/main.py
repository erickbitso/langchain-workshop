from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

model = ChatOpenAI(model="gpt-4")

memory = MemorySaver()

tools = [multiply]

agent_executor = create_react_agent(model, tools, checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="What is 3 times 4?")]}, config
):
    print(chunk)
    print("----")

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="What was the result of the last multiplication?")]}, config
):
    print(chunk)
    print("----")

