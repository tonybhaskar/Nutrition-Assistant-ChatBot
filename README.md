
# AI-Powered Context-Aware Chatbot

## Description

This project is a Python-based AI chatbot that utilizes the **Ollama** and **Groq** models to provide a context-aware conversation experience. 
The chatbot is capable of remembering the entire conversation history to deliver meaningful and relevant responses.

## Features

- **Context Awareness:** Maintains memory of previous messages to provide coherent responses.
- **Ollama Embeddings:** Utilizes `nomic-embed-text:latest` for high-quality text embeddings.
- **Groq Model Integration:** Uses `llama-3.3-70b-versatile` for generating accurate and contextual responses.
- **Vector Database:** Stores and retrieves conversation history for persistent memory.
- **Flask-Based UI:** Provides a web-based interface for easy interaction.

## Installation

To set up the project, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/context-aware-chatbot.git
cd context-aware-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root and add the following variables:

```bash
OLLAMA_MODEL=nomic-embed-text:latest
GROQ_MODEL=llama-3.3-70b-versatile
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

## Usage

### Running the Chatbot

```bash
python app.py
```

Once the server is running, open your browser and navigate to `http://127.0.0.1:5000` to start chatting.

## API Endpoints

| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| `/chat`         | POST   | Sends user input and receives AI response |
| `/history`      | GET    | Retrieves chat history |
| `/reset_memory` | POST   | Clears conversation memory |

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Ollama** for embeddings
- **Groq** for LLM responses
- **LangChain** for RAG-based retrieval
