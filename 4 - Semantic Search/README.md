# Semantic Search with LangChain

This project demonstrates how to perform semantic search on a PDF document using LangChain components. The goal is to build a pipeline that loads a document, processes it into manageable chunks, creates semantic embeddings, and retrieves relevant text based on user queries.

## What We Learn

- **Document Loading**  
  We use [`PyPDFLoader`](myenv/lib/python3.9/site-packages/langchain_community/document_loaders/hugging_face_model.py) to load and extract pages from a PDF (in this case, the Nike 10-K report).

- **Text Splitting**  
  The document is divided into smaller chunks using [`RecursiveCharacterTextSplitter`](myenv/lib/python3.9/site-packages/langchain_text_splitters/__init__.py). This makes it easier to process and embed large texts.

- **Generating Embeddings**  
  With [`OpenAIEmbeddings`](myenv/lib/python3.9/site-packages/langchain_openai/__init__.py), we generate vector embeddings from the text chunks. These embeddings capture the semantic meaning of the text.

- **Storing in a Vector Store**  
  The generated embeddings are stored in an in-memory vector store using [`InMemoryVectorStore`](myenv/lib/python3.9/site-packages/langchain_core/vectorstores/__init__.py), which allows for efficient similarity searches.

- **Similarity Search and Retrieval**  
  The script performs similarity searches to find the most relevant document chunks for given queries and demonstrates how to retrieve both individual results and batch results by converting the vector store into a retriever.

## Goal

The primary goal of this exercise is to illustrate how to:
- Process unstructured documents by loading and splitting text.
- Generate semantic embeddings that represent text meaning.
- Use vector similarity to retrieve relevant information from large documents.

This provides a solid foundation for building applications like document Q&A systems, search engines, and other tools that rely on semantic understanding.

## How to Run

1. **Setup:** Ensure you have the required dependencies installed as per the `requirements.txt`.
2. **API Key:** When running the script, you'll be prompted to enter your OpenAI API key if it isn't already set.
3. **Execution:** Run the script from the command line:
   ```sh
   python main.py
   ```
