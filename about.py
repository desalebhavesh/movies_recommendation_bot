import streamlit as st

def about_section():
    st.title("About the Movie Chatbot")

    st.markdown("""
    ### Project Breakdown:

    📊 **Dataset**:  
    The dataset forms the core of this project, containing valuable information related to movies for training:
    
    - **Intents**: The purpose of user input, such as:
        - Movie search queries
        - Movie details requests
        - Genre-specific requests (e.g., Hollywood, Bollywood, etc.)
        - Actor or director-specific queries
        - Trending or recently released movies
    - **Entities**: Specific information extracted from user input, such as:
        - Movie names (e.g., "Inception", "Titanic")
        - Movie genres (e.g., Action, Drama, Comedy)
        - Actor names (e.g., Leonardo DiCaprio, Tom Cruise)
        - Release years (e.g., 2020, 1995)
        - Popular movie categories (e.g., Trending, Top Rated)
    - **Text**: Raw user input, such as "Find me movies starring Tom Hanks" or "Tell me about the movie Titanic."
    
    💻 **Streamlit Interface**:  
    The Streamlit interface offers an easy and interactive way for users to get movie-related information:
    
    - A text input box where users can search for movies, inquire about movie details, or request movie recommendations.
    - A response area where the AI provides insights:
        - For movie searches: Displays movie titles, descriptions, and ratings.
        - For movie details: Provides detailed information about the movie, such as cast, plot summary, release year, and ratings.
        - For genre-based or actor-based recommendations: Suggests relevant movies.
    - Integrated with the trained NLP model and external APIs (such as TMDB) to deliver accurate and real-time movie information.
    
    ✅ **Conclusion**:  
    This project successfully combines Natural Language Processing (NLP) and AI to build a Movie Chatbot that provides users with quick, accurate, and tailored movie-related information.
    
    **Key Achievements**:
    - Utilized NLP techniques to interpret user inputs related to movies.
    - Built a user-friendly interface using Streamlit, enabling seamless interaction with the chatbot.
    - Leveraged APIs like TMDB to enrich the chatbot's responses with real-time movie data.
    - Demonstrated the potential for future enhancements, such as:
        - Integrating more movie databases for better coverage.
        - Expanding to include TV shows, documentaries, and other media.
        - Adding multilingual support to broaden accessibility.
    
    This project is a step forward in combining AI and user-focused design to enhance the movie-watching experience.
    """)

# Call the about_section function to display the content
if __name__ == "__main__":
    about_section()
    
    
