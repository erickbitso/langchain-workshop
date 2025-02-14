# Chatbot Training Section

This section is designed to help you understand how to build chatbots that can work both without and with memory. The examples demonstrate two important approaches:

1. **Stateless Chat Calls vs. Stateful Conversations**  
   - In [ex1.py](6 - Chatbot/ex1.py), you see a simple invocation of a chat model where each call is independent—there is no persistent memory of previous messages. The script contrasts a plain request (stateless) with a call that manually chains previous messages (stateful) to simulate a conversation history.
  
2. **Graph-Based Workflows and Automatic Memory Management**  
   - In [ex2.py](6 - Chatbot/ex2.py), the example introduces advanced conversation flow management using a state graph (`StateGraph`) and a memory saver (`MemorySaver`). This approach automatically updates the conversation state and reuses past messages, showing how to maintain a more robust dialogue context.

## Topics Covered

- **Chat Model Initialization**  
  How to initialize a chat model (using `init_chat_model`) and set up the environment (e.g., API key management).

- **Stateless vs. Stateful Invocations**  
  Comparing simple, one-off invocations with approaches that preserve conversation history, allowing the model to "remember" details from previous interactions.

- **Memory Integration**  
  Techniques to incorporate memory into chatbots, including manually chaining messages and using dedicated memory managers such as `MemorySaver`.

- **State Graph and Workflow Management**  
  Introduction to constructing workflows (via `StateGraph` and `MessagesState`) that manage conversation state automatically, which is essential for more complex conversational applications.

This training section ultimately aims to equip you with both the fundamentals and advanced patterns for developing chatbots that can adapt to varied dialogue requirements using LangChain's powerful tools.