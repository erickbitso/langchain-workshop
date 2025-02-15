# Tool Calling Training Session

## Overview

In this session, we explore how to integrate custom tools with a language model using LangChain. We demonstrate how to bind a Python function as a tool and have the LLM invoke it during processing.

## Goals

- **Understand Tool Binding:**  
  Learn how to associate a custom function (in this example, `multiply`) with the language model so that it can be invoked as a tool.
  
- **Simulate LLM-Driven Tool Calls:**  
  See how the LLM can be used to interpret a query, generate a tool call request, and how you can manually execute that tool call.

- **Enhance LLM Capabilities:**  
  Learn to extend the functionality of LLMs by integrating them with external logic, enabling richer and more interactive applications.

## Code Explanation

- **Defining a Tool**  
  The `multiply` function is defined to perform a simple multiplication of two integers.

- **LLM Initialization and Tool Binding**  
  A [ChatOpenAI](langchain_openai/ChatOpenAI) model is instantiated and bound with the `multiply` tool using the `bind_tools` method. This allows the model to recognize and suggest the tool for appropriate queries.

- **Invoking the Tool**  
  The model is then given the query "What is 3 times 4?". The system generates a tool call request (`msg.tool_calls`), which is executed manually by checking if the tool call matches "multiply" and then calling the function with the provided arguments.

- **Output Details**  
  The output displays both the tool call metadata and the result of executing the tool.

## How to Run

1. Open your terminal in the workspace directory.
2. Ensure you have the necessary dependencies installed.
3. Run the script:
   ```sh
   python main.py
   ```
