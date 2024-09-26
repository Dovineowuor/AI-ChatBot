# src/engine.py

from chatbot import Chatbot

class ChatbotEngine:
    def __init__(self, model_id):
        """Initialize the chatbot engine."""
        self.chatbot = Chatbot(model_id)

    async def handle_message(self, message, chat_history=[]):
        """Handle a user message and return the bot's response."""
        return await self.chatbot.chat_function_with_emotions(message, chat_history)
