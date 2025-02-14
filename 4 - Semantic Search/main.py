from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
import getpass
import os

# Prompt the user to enter the OpenAI API key if it's not already set in the environment variables
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Define the path to the PDF document to be loaded
file_path = "../docs/nke-10k-2023.pdf"

# Load the PDF document using PyPDFLoader
loader = PyPDFLoader(file_path)
docs = loader.load()
print(f"Number of pages loaded: {len(docs)}")

# Split the document into smaller chunks using RecursiveCharacterTextSplitter
# This helps in processing large documents by breaking them into manageable pieces
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)
print(f"Number of chunks created: {len(all_splits)}")

# Initialize the OpenAIEmbeddings model for generating text embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Create an in-memory vector store to store the document embeddings
vector_store = InMemoryVectorStore(embeddings)

# Add the document chunks to the vector store and generate their embeddings
ids = vector_store.add_documents(documents=all_splits)

# Perform a similarity search to find the most relevant document chunk for the given query
results = vector_store.similarity_search(
    "How many distribution centers does Nike have in the US?"
)
print(f"Most relevant document chunk: {results[0]}")

# Perform a similarity search with score to get the relevance score along with the document chunk
results = vector_store.similarity_search_with_score("What was Nike's revenue in 2023?")
doc, score = results[0]
print(f"Relevance Score: {score}\n")
print(f"Document chunk: {doc}")

# Create a retriever from the vector store for batch processing of multiple queries
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)

# Perform batch retrieval for multiple queries
batch_results = retriever.batch(
    [
        "How many distribution centers does Nike have in the US?",
        "When was Nike incorporated?",
    ],
)
print(f"Batch retrieval results: {batch_results}")