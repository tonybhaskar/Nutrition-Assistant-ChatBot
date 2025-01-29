from langchain_community.document_loaders import WebBaseLoader
from langchain.schema import Document

def load_and_clean_data(url):
    # Load data from the web
    docs = WebBaseLoader(url).load()
    
    # Clean the data
    cleaned_documents = []
    for doc in docs:
        cleaned_content = " ".join(doc.page_content.split())
        # Ensure the content is relevant and comprehensive
        if cleaned_content:  # Only add non-empty content
            cleaned_documents.append(Document(page_content=cleaned_content, metadata=doc.metadata))
    
    return cleaned_documents