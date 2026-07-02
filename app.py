from annotated_types import doc
import chromadb
chroma_client = chromadb.Client()
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile
from langchain_google_genai import GoogleGenerativeAIEmbeddings


embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
#collection = chroma_client.create_collection(name="my_collection")

# collection.add(
#     ids=["id1", "id2"],
#     documents=[
#         "This is a document about pineapple",
#         "This is a document about oranges"
#     ]
# )

document = [
    {"id": "id1", "document": "This is a document about pineapple"},
    {"id": "id2", "document": "This is a document about oranges"} 
]

SAMPLE_DOCS = [
    Document(page_content="LangChain is a framework for LLM applications.", metadata={"source":"doc1"}),
    Document(page_content="Python is a programming language.", metadata={"source":"doc2"}),
    Document(page_content="Chroma is a vector database.", metadata={"source":"doc3"})
]

collection_name = "my_collection"

def get_or_create_collection(collection_name,document):
    try:
        collection = chroma_client.get_collection(collection_name)
        print(f"Collection '{collection_name}' already exists.")
    except Exception as e:
        print(f"Collection '{collection_name}' does not exist. Creating a new collection.")
        collection = chroma_client.create_collection(name=collection_name)
    
    for doc in document:
        collection.upsert(ids=doc["id"], documents={doc["document"]})
    result = collection.query(
        query_texts=["pineapple"], #query_texts=query
        n_results=2
    )
    return print(result)
    
def chroma_basics():
    with tempfile.TemporaryDirectory() as tmpdir:
        
        vectorstore = Chroma(document=SAMPLE_DOCS, persist_directory=tmpdir, embedding_function=embeddings)
        print(f"Vectorstore created {vectorstore._collection.count()} and persisted in temporary directory:", tmpdir)

if __name__ == "__main__":
    chroma_basics()