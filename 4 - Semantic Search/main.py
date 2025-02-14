from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Loads the document
file_path = "../docs/nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
print(len(docs))


# Splits the document into chunks using the RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

print(len(all_splits))
