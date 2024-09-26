# src/chatbot.py

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import spacy
from nltk import download
from nltk.corpus import wordnet

# Download necessary NLTK resources
download('wordnet')

class Chatbot:
    def __init__(self, model_id):
        """Initialize the chatbot with a Hugging Face model."""
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")
        self.nlp = spacy.load('en_core_web_sm')
        self.emotion_analyzer = pipeline(
            'text-classification',
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None,
            device=0 if torch.cuda.is_available() else -1
        )
        self.response_cache = {}

    def analyze_emotion(self, message):
        """Analyze the emotion of the message."""
        results = self.emotion_analyzer(message)
        if isinstance(results, list) and len(results) > 0 and isinstance(results[0], dict):
            label = results[0].get('label', 'unknown')
            score = results[0].get('score', 0.0)
        else:
            label = 'unknown'
            score = 0.0
        return label.lower(), score

    def extract_keywords(self, text):
        """Extract keywords from the text."""
        doc = self.nlp(text)
        keywords = []
        for token in doc:
            if token.pos_ in ['NOUN', 'VERB', 'ADJ'] and not token.is_stop and not token.is_punct:
                keywords.append(token.text.lower())
                for syn in wordnet.synsets(token.text):
                    for lemma in syn.lemmas():
                        synonyms = lemma.name().lower()
                        if synonyms not in keywords:
                            keywords.append(synonyms)
        return keywords

    async def generate_response(self, message, max_tokens=400, temperature=0.7, top_p=0.9):
        """Generate a response using the model."""
        input_ids = self.tokenizer.encode(message, return_tensors="pt")
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        input_ids = input_ids.to(device)

        try:
            output = self.model.generate(
                input_ids,
                max_length=max_tokens,
                num_beams=5,
                no_repeat_ngram_size=2,
                temperature=temperature,
                top_p=top_p
            )
        except RuntimeError as e:
            if "CUDA out of memory" in str(e):
                return "Sorry, the model ran out of memory. Please try with a smaller input or on a different device."
            else:
                raise e

        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    async def chat_function_with_emotions(self, message, chat_history=[]):
        """Handle the chat functionality with emotion analysis and response generation."""
        emotion_label, emotion_score = self.analyze_emotion(message)
        response = await self.generate_response(message)

        # Emotion-aware response adjustments
        if emotion_label in ['joy', 'satisfaction']:
            response = f"Glad to hear you're feeling great! 😊 {response}"
        elif emotion_label in ['sadness', 'frustration']:
            response = f"I'm really sorry you're feeling this way. How can I assist you better? 💔 {response}"
        elif emotion_label == 'anger':
            response = f"I sense some frustration. Let’s work through this together! 💪 {response}"
        elif emotion_label == 'fear':
            response = f"It's okay to feel that way. I'm here to help. 🙏 {response}"

        # Update chat history
        chat_history.append((message, response))
        self.response_cache[message] = response
        return "", chat_history
