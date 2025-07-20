import nltk
import random
import string
nltk.download('wordnet')
nltk.download('punkt', download_dir=r"C:\Users\karthi D\AppData\Roaming\nltk_data")

from nltk.stem import WordNetLemmatizer
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm a bot, but I'm doing great! Thanks for asking.",
    "what is your name": "I'm CodBot, your internship assistant.",
    "bye": "Goodbye! Have a nice day.",
    "default": "Sorry, I didn't understand that. Can you rephrase?"
}

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    return [lemmatizer.lemmatize(word) for word in tokens]

def respond(user_input):
    cleaned = clean_text(user_input)
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return responses["default"]

print("CodBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("CodBot:", responses["bye"])
        break
    response = respond(user_input)
    print("CodBot:", response)
