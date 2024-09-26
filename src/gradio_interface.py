# src/gradio_interface.py

import gradio as gr
from core.engine import ChatbotEngine

# Initialize the chatbot engine with the model ID
model_id = "NousResearch/Llama-2-7b-chat-hf"
chatbot_engine = ChatbotEngine(model_id)

# Define the Gradio interface
with gr.Blocks() as interface:
    gr.Markdown(
        """
        # Welcome to DoveAI StudyMate Bot 📚🤖

        Welcome to the **DoveAI StudyMate Bot** project! This interactive chatbot is designed to support students in their learning journey by providing personalized guidance, answering questions, and offering encouragement. The bot leverages natural language processing (NLP) models, such as `transformers` and `spacy`, to understand user queries, analyze emotions, and generate meaningful responses.
        """
    )

    chatbot = gr.Chatbot(
        label="Chat with The Dove",
        value=[
            ("Hello! How can I assist you today?", None),  # Initial bot message
        ],
        elem_id="chatbot"  # CSS ID for additional styling if needed
    )

    with gr.Row():
        text_input = gr.Textbox(show_label=False, placeholder="Type a message and hit enter...")
        text_input.submit(
            chatbot_engine.handle_message, [text_input, chatbot], [text_input, chatbot]
        )

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch(debug=True)
