import nltk
nltk.download('punkt')
import nltk
import random
import string

# Sample responses for the chatbot
responses = {
    "greet": ["Hello! How can I help you today?", "Hi there! How can I assist you?", "Greetings! How can I be of service?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "default": ["I'm sorry, I don't understand that.", "Can you please rephrase?", "I'm not sure I understand."]
}

# Keywords for recognizing user intent
keywords = {
    "greet": ["hello", "hi", "greetings", "hey",],
    "goodbye": ["bye", "goodbye", "see you", "later"]
}

def preprocess_input(user_input):
    user_input = user_input.lower()
    user_input = nltk.word_tokenize(user_input)
    return user_input

def get_response(user_input):
    user_input = preprocess_input(user_input)
    for intent, keywords_list in keywords.items():
        for word in user_input:
            if word in keywords_list:
                return random.choice(responses[intent])
    return random.choice(responses["default"])

def chatbot():
    print("Chatbot: Hi! I'm a chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()



