# DoveAI Chat Agent 🤖💬

Welcome to the **DoveAI Chat Agent**! This advanced AI chatbot is designed to provide insightful, emotion-aware responses to user queries, making learning and interaction a more engaging experience. By leveraging state-of-the-art language models and emotion detection techniques, our chatbot offers personalized interactions, contextually accurate answers, and dynamic user engagement.

## Key Features

- **Emotion-Aware Responses**: The chatbot adapts its responses based on the user's emotional state, ensuring a supportive and empathetic interaction through a sophisticated emotion detection model.

- **Contextual Understanding**: Utilizing a Retrieval-Augmented Generation (RAG) approach, the chatbot provides relevant and contextually accurate answers by enhancing language generation with external knowledge sources.

- **Keyword Extraction**: Employs advanced NLP techniques to extract key terms and synonyms, significantly improving question understanding and response relevance.

- **Dynamic Interaction**: Fetches jokes, personalized content, and relevant information based on specific keywords, making conversations lively and engaging.

- **Customizable Knowledge Base**: The QA dataset can be easily updated, allowing the chatbot to grow its knowledge base over time and adapt to new topics.

- **User-Friendly Interface**: Built with Gradio, the chatbot offers a simple, intuitive interface that allows users of all tech levels to engage seamlessly.

## Project Structure

```/ai_chat_bot
├── notebooks/                  # Jupyter notebooks for experiments and demonstrations
│   └── HuggingFaceStackUp.ipynb
├── data/                       # Data files for QA
│   └── qa_dataset.csv          # CSV file for questions and answers
├── src/                        # Source code for the chatbot and Gradio interface
│   ├── chatbot.py              # Core chatbot logic
│   └── gradio_interface.py     # Gradio interface for user interaction
├── LICENSE                     # License file
├── README.md                   # Project description and instructions
├── requirements.txt            # List of dependencies
└── .gitignore                  # To exclude unnecessary files from Git tracking
```

## Installation

To set up and run the **Dove Chat Agent** locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/dovineowuor/ai-chatbot.git
cd ai-chatbot
```

### 2. Install Dependencies

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment

Ensure you have the necessary API tokens for Hugging Face and any other required credentials. You can set these as environment variables or store them in a `.env` file.

### 4. Run the Chatbot

To start the chatbot, you can either run the core logic:

```bash
python src/chatbot.py
```

Or launch the interactive Gradio interface:

```bash
python src/gradio_interface.py
```

## Usage

1. **Interact with the Chatbot**:
   - Once the Gradio interface is launched, open the provided URL in your browser to begin interacting with the chatbot. Simply type in your questions or comments, and the chatbot will respond accordingly.

2. **Update the Knowledge Base**:
   - To update the QA dataset with new questions and answers, modify the `qa_dataset.csv` file located in the `data/` directory or use the provided functions to add new entries. This allows the chatbot to stay up-to-date with relevant information.

## Contributing

We welcome contributions from everyone! Whether you encounter a bug, have a feature suggestion, or wish to improve the existing code, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Transformers** by Hugging Face for powering the language model and pipeline functionalities.
- **spaCy** for named entity recognition and other NLP utilities.
- **NLTK** for keyword processing and synonym generation using WordNet.
- **Gradio** for creating the interactive web interface that makes the chatbot accessible to everyone.

## Contact

For any questions, issues, or feedback, please reach out to [owuordove@gmail.com](mailto:owuordove@gmail.com). We’re here to help!

---

Enjoy your experience with the **DoveAI Chat Agent** and happy chatting! 🎉

