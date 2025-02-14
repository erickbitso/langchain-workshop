from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = OllamaLLM(model="llama3.2",
                temperature=0,
                max_new_tokens=512)

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template("Write me the lyrics for a 30 second jingle about {product}")


chain = prompt | llm | output_parser

# print(chain.invoke({"product": "Bitcoin"}))


for chunk in chain.stream({"product": "Bitcoin"}):
    print(chunk, end="", flush=True)
