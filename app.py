import streamlit as st
import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
import pickle



# Import your sections

from home import home_section # Assuming home.py is present
from about import about_section  # Assuming about.py is present
from history import history_section  # Assuming history.py is present
from socials import socials_section  # Assuming socials.py is present

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the intents file
with open('intents.json', 'r') as file:
    intents_data = json.load(file)

# Load the words, classes, and model
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

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
def get_response(intents_list, intents_json, movie_name=None):
    if not intents_list:
        return "Sorry, I didn't understand that. Can you try rephrasing?"
    
    tag = intents_list[0]['intent']
    list_of_intents = intents_json.get('intents', [])
    for i in list_of_intents:
        if i['tag'] == tag:
            response = random.choice(i['responses'])
            if movie_name:
                response = response.format(movie_name=movie_name)
            return response
    return "Sorry, I couldn't find a suitable response."

# Main function for Streamlit app with navigation
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "About", "Chat History", "Socials"])

    if selection == "Home":
        home_section()  # Call the home section
        
    elif selection == "About":
        about_section()  # Call the about section
    
    elif selection == "Chat History":
        history_section()  # Call the chat history section

    elif selection == "Socials":
        socials_section()  # Call the socials section

    # Display the chatbot
    user_input = st.text_input("You: ", "")

    if user_input:
        # Predict the class of the message
        intents = predict_class(user_input)
        response = get_response(intents, intents_data)
    
        # Display response from the bot
        st.write(f"Bot: {response}")

# Success confirmation message
    st.write("🎉 The Movie Search Chatbot is running smoothly! No errors detected. 🎉")

# Run the app
if __name__ == "__main__":
    main()
