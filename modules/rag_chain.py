# rag_chain.py

from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq.chat_models import ChatGroq
from langchain_core.output_parsers import StrOutputParser
# from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma
from config import Config


from modules.embeddings import setup_vector_store

def setup_rag_chain(documents):
    try:
        vector_store = setup_vector_store(documents)
        retriever = vector_store.as_retriever()
        print("Vector store loaded successfully.")
        
        # Define the RAG prompt template
        rag_template = """
            Give answers based on the context
            Context: 
            {context}

            Question: {question}
        """
        rag_prompt = ChatPromptTemplate.from_template(rag_template)
        
        # Set up the LLM
        llm = ChatGroq(temperature=0.2, model=Config.GROQ_MODEL)
        print("LLM set up successfully.")
        
        # Create the RAG chain
        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | rag_prompt
            | llm
            | StrOutputParser()
        )
        print("RAG chain created successfully.")
        return rag_chain
    except Exception as e:
        print(f"Error setting up RAG chain: {e}")
        raise
