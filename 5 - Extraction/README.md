# Information Extraction with LangChain

This project demonstrates how to extract structured information from unstructured text using LangChain components. The goal is to build a pipeline that prompts an LLM to extract relevant attributes and returns them as structured data using a defined schema.

## What We Learn

- **Structured Data Extraction**  
  We use a Pydantic model (`Person`) to define the schema for the information we want to extract from a text snippet. This ensures that the output follows a consistent structure.

- **Prompt Engineering**  
  With `ChatPromptTemplate`, we craft a prompt that instructs the LLM to act as an expert extraction algorithm. The prompt guides the model on which attributes to extract and how to handle missing values.

- **LLM Integration**  
  The project integrates a chat-based model initialized with LangChain (`init_chat_model`). The model is further configured to output structured responses with the given schema, ensuring that the extracted data conforms to our expected format.

- **Environment Configuration**  
  Similar to other LangChain projects, the script prompts the user for an OpenAI API key if it's not found in the environment variables.

## Goal

The main objective of this exercise is to illustrate how to:
- Convert unstructured text into structured data using language models.
- Define and enforce a schema for the extracted data using Pydantic.
- Use prompt templates to reliably steer the model towards producing the desired output.

This approach lays the groundwork for building more complex information extraction systems, such as automated data entry from freeform text or building knowledge bases from reports.

## How to Run

1. **Setup:**  
   Ensure that you have the required dependencies installed as per the `requirements.txt`.

2. **API Key:**  
   When running the script, you'll be prompted to enter your OpenAI API key if it isn't already set in your environment.

3. **Execution:**  
   Run the script from the command line:
   ```sh
   python main.py