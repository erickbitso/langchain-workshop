from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

llm = ChatOpenAI(model="gpt-4")

tools = [multiply]

agent_executor = create_react_agent(llm, tools)

response = agent_executor.invoke({"messages": [HumanMessage(content="What is 3 times 4?")]})

print(response["messages"])
