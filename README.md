___
# DoveAI Chat Agent

The **DoveAI Chat Agent** is an advanced AI chatbot designed to provide insightful, emotion-aware responses to user queries. Leveraging state-of-the-art language models and emotion detection, the chatbot offers personalized interactions, contextually accurate answers, and dynamic user engagement.

## Key Features

- **Emotion-Aware Responses:** The chatbot adapts its responses based on the user's emotional state using a sophisticated emotion detection model.
- **Contextual Understanding:** Employs a Retrieval-Augmented Generation (RAG) approach to provide relevant and contextually accurate answers by augmenting language generation with external knowledge sources.
- **Keyword Extraction:** Uses NLP techniques to extract key terms and synonyms for improved question understanding and response relevance.
- **Dynamic Interaction:** Capable of fetching jokes and personalized content based on specific keywords to make interactions more engaging.
- **Customizable Knowledge Base:** The QA dataset can be easily updated, allowing the chatbot to grow its knowledge base over time.

## Project Structure

```
/ai_chat_bot
├── notebooks/                  # Jupyter notebooks
│   └── HuggingFaceStackUp.ipynb
├── data/                       # Data files for QA
│   └── qa_dataset.csv
├── src/                        # Source code for the chatbot and Gradio interface
│   ├── chatbot.py              # Core chatbot logic
│   └── gradio_interface.py     # Gradio interface for interaction
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

Ensure that you have the necessary API tokens for Hugging Face and any other required credentials. These can be set as environment variables or stored in a `.env` file.

### 4. Run the Chatbot

To start the chatbot, you can either run:

```bash
python src/chatbot.py
```

Or launch the interactive Gradio interface:

```bash
python src/gradio_interface.py
```

## Usage

1. **Interact with the Chatbot:**
   - Once the Gradio interface is launched, open the provided URL in your browser to begin interacting with the chatbot.
   
2. **Update the Knowledge Base:**
   - To update the QA dataset with new questions and answers, modify the `qa_dataset.csv` file located in the `data/` directory or use the provided functions to add new entries.

## Contributing

Contributions are welcome! Whether you find a bug, have a suggestion for a new feature, or want to improve the existing code, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Transformers** by Hugging Face for powering the language model and pipeline functionalities.
- **spaCy** for named entity recognition and NLP utilities.
- **NLTK** for wordnet synonyms and keyword processing.
- **Gradio** for the interactive web interface.

## Contact

For any questions, issues, or feedback, please reach out to [owuordove@gmail.com](mailto:owuordove@gmail.com).

---
