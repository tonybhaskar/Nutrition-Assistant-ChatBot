from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify
# from langchain_community.document_loaders import WebBaseLoader
# from langchain.schema import Document
from modules.data_loader import load_and_clean_data
# from langchain_community.vectorstores import Chroma
# from langchain_ollama import OllamaEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from config import Config
from modules.embeddings import setup_vector_store
# from langchain.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_groq.chat_models import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
from modules.rag_chain import setup_rag_chain
# from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from modules.chat_history import ChatHistory

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load and clean documents
url = "https://en.wikipedia.org/wiki/Human_nutrition"
cleaned_documents = load_and_clean_data(url=url)

# Setup vector store
success = setup_vector_store(documents=cleaned_documents)
print("Vector store setup:", success)

# Initialize RAG chain
chain = setup_rag_chain(documents=cleaned_documents)

# Initialize chat history
history = ChatHistory()

def get_input_string(history):
    input_string = "\n".join([f"{msg.__class__.__name__.replace('Message', '')}: {msg.content}" for msg in history])
    return input_string

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user's question
        user_input = request.json.get("message")
        
        if not user_input:
            return jsonify({"response": "Please provide a message."})
        
        # Add user message to chat history
        history.add_user_message(user_input)
        
        # Generate the input string for context
        input_string = get_input_string(history=history.get_history())
        
        # Generate response using RAG chain
        response = chain.invoke(input_string)
        
        # Add assistant message to chat history
        history.add_assistant_message(response)
        
        # Return the response as JSON
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
