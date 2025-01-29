# embeddings.py

from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import Config
import chromadb
from uuid import uuid4

def get_embedding_function():
    return OllamaEmbeddings(
        base_url=Config.OLLAMA_BASE_URL,
        model=Config.OLLAMA_MODEL
    )

def setup_vector_store(documents):
    try:
        if not documents or len(documents) == 0:
            print("❌ No documents provided for embedding.")
            return False

        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=650,
            chunk_overlap=150
        )
        doc_splits = text_splitter.split_documents(documents)
        print(f"✅ Documents split into {len(doc_splits)} chunks.")
        uuids = [str(uuid4()) for _ in range(len(doc_splits))]


        persistent_client = chromadb.PersistentClient()
        collection = persistent_client.get_or_create_collection("rag_chroma")
        vector_store_from_client = Chroma(
            client=persistent_client,
            collection_name="rag_chroma",
            embedding_function= get_embedding_function()
        )

        vector_store_from_client.add_documents(documents=doc_splits, ids=uuids)


        print("✅ Vector store persisted successfully.")

        return vector_store_from_client
    except Exception as e:
        print(f"❌ Error in setup_vector_store: {e}")
        return False
