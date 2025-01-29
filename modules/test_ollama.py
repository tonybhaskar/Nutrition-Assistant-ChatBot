# test_ollama.py
from langchain_ollama import OllamaEmbeddings

def test_ollama():
    try:
        embeddings = OllamaEmbeddings(
            base_url="http://127.0.0.1:11434",
            model="nomic-embed-text:latest"
        )
        result = embeddings.embed_documents(["Hello, world!"])
        print("Ollama connection successful! Result:", result)
    except Exception as e:
        print("Ollama connection failed:", e)

if __name__ == "__main__":
    test_ollama()