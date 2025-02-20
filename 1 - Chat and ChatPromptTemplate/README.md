# Chat Prompts and Prompt Templates - Technical Lesson

This lesson demonstrates how to build chat prompts and use prompt templates with LangChain. You'll learn how to:
- Configure and set up environment variables.
- Create custom chat prompts using the [`ChatPromptTemplate`](langchain_core/prompts) class.
- Chain a prompt template with a language model, such as [`OllamaLLM`](langchain_ollama/llms), for interactive Q&A.

## Overview

In this lesson, we cover:
- **Environment Setup:**  
  Using `getpass` and environment variables to securely input API keys. See [message_list.ipynb](1%20-%20Chat%20and%20ChatPromptTemplate/message_list.ipynb).

- **Prompt Template Creation:**  
  Creating a prompt template with a custom template that guides the model step-by-step. Check out [prompt_template.py](1%20-%20Chat%20and%20ChatPromptTemplate/prompt_template.py).

- **Model Chaining:**  
  Combining the prompt template with a language model to form a processing chain that can answer questions interactively.

## Files

- **[message_list.ipynb](1%20-%20Chat%20and%20ChatPromptTemplate/message_list.ipynb):**  
  Sets up the environment and initializes the chat model.

- **[prompt_template.py](1%20-%20Chat%20and%20ChatPromptTemplate/prompt_template.py):**  
  Contains the implementation of a prompt template that is chained with a language model to answer queries.

- **[prompt_template.ipynb](1%20-%20Chat%20and%20ChatPromptTemplate/prompt_template.ipynb):**  
  A notebook version that demonstrates the usage and output of the prompt template integration.

