# Structured Output Training

This part of the training focuses on how to generate structured output from language models using prompt chaining and output parsing. We explore two examples:

- **Extraction with OllamaLLM** ([example3/ex1.py](example3/ex1.py))
- **Classification with ChatOpenAI** ([example3/ex2.py](example3/ex2.py))

## Topics Covered

- **Prompt Chaining:**  
  Using [`ChatPromptTemplate`](langchain_core/prompts) to create prompts that guide the model on how to generate the expected output.

- **Structured Output Format:**  
  Two examples show how to enforce and parse a specific JSON or Pydantic schema:
  - In the first example ([example3/ex1.py](example3/ex1.py)), the output is expected to be JSON matching a defined schema.
  - In the second example ([example3/ex2.py](example3/ex2.py)), a Pydantic model (`Classification`) is used to ensure the output conforms to a specific structure.

- **LLM Integration:**  
  - Using [`OllamaLLM`](langchain_ollama/llms) to interact with one model (e.g. `llama3.2`).
  - Using [`ChatOpenAI`](langchain_openai) to call a chat-based language model (e.g. `gpt-3.5-turbo`) with structured output enabled.

- **Output Parsing:**  
  The examples demonstrate how to use output parsers ([`JsonOutputParser`](langchain_core/output_parsers)) to convert raw responses into structured data.

## Goals

- **Understanding Structured Output:**  
  Learn how to design prompts and parse responses so that a language model returns output in the desired structured format.

- **Schema Enforcement:**  
  See how JSON schemas and Pydantic models can be used to strictly define acceptable output, ensuring consistency and reliability in data extraction tasks.

- **Applying in Real-World Use Cases:**  
  Understand the pipeline of chaining prompts with LLMs and parsers for tasks such as information extraction and text classification.

By working through these examples, you'll gain practical experience with setting up prompt templates, working with different language model integrations, and enforcing structured formatting on generated responses.