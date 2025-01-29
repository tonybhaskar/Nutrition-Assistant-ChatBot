# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "nomic-embed-text:latest")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")