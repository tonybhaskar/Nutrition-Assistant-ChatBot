from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class ChatHistory:
    def __init__(self):
        # Initialize with a system message (in object form)
        self.history = [SystemMessage(content='You are a helpful assistant that answers questions about human nutrition.')]

    def add_user_message(self, message):
        """Adds a user message and returns the updated chat history string."""
        # Store the user message as a HumanMessage object
        self.history.append(HumanMessage(content=message))
        
        # Format the conversation history as a string
        input_string = "\n".join([f"{msg.__class__.__name__.replace('Message', '')}: {msg.content}" for msg in self.history])
        return input_string  # Return formatted string
    
    def add_assistant_message(self, response):
        """Adds an assistant (AI) message to the chat history."""
        self.history.append(AIMessage(content=response))

    def get_history(self):
        """Returns the full chat history as a list of message objects."""
        return self.history
    
