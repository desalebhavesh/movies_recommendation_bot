import os
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model  # type: ignore
import streamlit as st

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the intents JSON file
try:
    with open('D:\chatbot\intents.json', 'r') as file:
        intents_data = json.load(file)
except FileNotFoundError:
    print("Error: 'intents.json' file not found. Ensure the file exists at the specified path.")
    exit()
except json.JSONDecodeError:
    print("Error: Failed to parse 'intents.json'. Ensure it is a valid JSON file.")
    exit()

# Load the words, classes, and model
try:
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    model = load_model('chatbot_model.h5')
except FileNotFoundError as e:
    print(f"Error: {e.filename} file not found. Ensure all necessary files are in place.")
    exit()

# Function to clean up the sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# Function to create a bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Function to predict the class of the sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Function to get the response based on the predicted intent
def get_response(intents_list, intents_json):
    if not intents_list:
        return "Sorry, I didn't understand that. Can you try rephrasing?"
    
    tag = intents_list[0]['intent']
    list_of_intents = intents_json.get('intents', [])
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "Sorry, I couldn't find a suitable response."

# Main loop for the chatbot
print("Movie Search Chatbot is running... Type 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        break
    
    # Predict the class of the message
    intents = predict_class(user_input)
    response = get_response(intents, intents_data)
    
    print(f"Bot: {response}")

# Print a message at the end to confirm the program ran
print("Chatbot session ended.")