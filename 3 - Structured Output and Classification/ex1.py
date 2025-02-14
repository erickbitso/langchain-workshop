import json
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

output_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "favorite_food": {
            "type": "string",
        },
    },
    "required": ["name", "age"],
}

output_schema_as_string = json.dumps(output_schema, indent=2)

llm = OllamaLLM(
    model="llama3.2",
    format="json",
    temperature=0.1,
    max_new_tokens=512
    )
messages = [
    ("system", 
         "You are a helpful assistant that will extract information about a person and produce "
         "an output using the following json schema: {json_schema}"),
    ("human", "{person_info}"),
]

prompt = ChatPromptTemplate.from_messages(messages)
chain = prompt | llm | JsonOutputParser()

response = chain.invoke(
    {
        "json_schema": output_schema_as_string,
        "person_info": "Erick is 40 and loves tacos"
    })

print(response)
print(type(response))