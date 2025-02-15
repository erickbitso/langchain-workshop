from langchain_openai import ChatOpenAI


# Define a tool
def multiply(a: int, b: int) -> int:
    return a * b

llm = ChatOpenAI(model="gpt-4")

llm_with_tools = llm.bind_tools([multiply])

msg = llm_with_tools.invoke("What is 3 times 4?")

print(f"ToolCalls: {msg.tool_calls}")

# Execute the tool call manually
tool_call = msg.tool_calls[0]
if tool_call["name"] == "multiply":
    result = multiply(**tool_call["args"])
    print(f"Result: {result}")
