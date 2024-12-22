import streamlit as st

# Function for the chatbot search section
def chat_with_bot():
    st.subheader("🎬 Let's Talk Movies!")
    st.write("Type your movie-related query below.")

    user_input = st.text_input("Enter your movie preferences or questions:")
    if user_input:
        # Placeholder for the chatbot's response, you can integrate actual chatbot logic here
        st.write(f"🔍 Searching for movies related to: {user_input}")
        # Here you can add the logic for movie search or recommendation based on the user_input

def home():
    # Adding a title with an image
    col1, col2 = st.columns([1, 3])

    # Add an image in the first column
    with col1:
        st.image("D:\chatbot\Movie bot.jpg", use_column_width=True)

    # Add the title in the second column
    with col2:
        st.title("🎥 Movies Recommendation Bot")
        st.write(
            """
            Your personal assistant for discovering amazing movies!  
            - Get personalized recommendations.  
            - Find details about your favorite movies.  
            - Explore genres, ratings, and cast.  
            """
        )

    # Add a fancy divider
    st.markdown("---")

    st.subheader("✨ Features:")
    st.write(
        """
        - **Personalized Recommendations:** Based on your preferences.  
        - **Detailed Information:** Genres, cast, ratings, and more.  
        - **Interactive Chat:** Ask questions and get instant answers.  
        """
    )

    # Add a button to start chatting
    if st.button("🚀 Start Chatting"):
        chat_with_bot()  # Redirect to the bot search section

# Call the home function to run it
if __name__ == "__main__":
    home()


# home.py
def home_section():
    return "This is the home section!"