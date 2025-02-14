import getpass
import os
from langchain_core.messages import HumanMessage

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")
from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Doesn't remember
print(model.invoke([HumanMessage(content="Hi! I'm Bob")]).content)
print(model.invoke([HumanMessage(content="What's my name?")]).content)


# Now let's enable memory for it
