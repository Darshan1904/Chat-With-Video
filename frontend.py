import streamlit as st
import random
import requests
import json

# Function to fetch transcripts from Flask API
def fetch_transcripts(video_url):
    try:
        response = requests.post("http://127.0.0.1:5000/transcribe", json={"videoURL": video_url})
        if response.status_code == 200:
            return response.json().get('summary')
        else:
            return f"Error: {response.json().get('error', 'An error occurred.')}"
    except Exception as e:
        return f"An error occurred: {e}"

# Function to query transcripts from Flask API
def query_transcripts(question):
    try:
        response = requests.post("http://127.0.0.1:5000/query", json={"query": question})
        if response.status_code == 200:
            return response.json().get('result')
        else:
            return f"Error: {response.json().get('error', 'An error occurred.')}"
    except Exception as e:
        return f"An error occurred: {e}"

# Dummy replies array (as fallback)
dummy_replies = [
    "That's a great question! The answer is quite simple...",
    "I believe the video explains this point around the 5-minute mark.",
    "This concept is explained in detail in the transcripts.",
    "Please refer to the section where the speaker talks about this topic.",
    "I'm not sure, but let me look into it and get back to you.",
    "This is a bit complex, but I'll try to simplify it for you..."
]

# Function to get a dummy answer (as fallback)
def get_dummy_answer(question):
    return random.choice(dummy_replies)

st.title("Engage Smarter, Not Longer")

st.sidebar.header("Provide the Link")
video_url = st.sidebar.text_input("Enter YouTube URL")
fetch_video_button = st.sidebar.button("Fetch Video")
if fetch_video_button and video_url:
    try:
        st.session_state.video_url = video_url
        st.session_state.transcripts = fetch_transcripts(video_url)
    except Exception as e:
        st.error(f"Failed to load video: {e}")

# Display video and transcripts if available
if 'video_url' in st.session_state:
    st.video(st.session_state.video_url)
if 'transcripts' in st.session_state:
    st.subheader("Summary")
    st.text_area("", st.session_state.transcripts, height=300)

# Chat section
st.subheader("Chat with Video")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Handle form submission without page refresh
with st.form(key='chat_form'):
    user_question = st.text_input("Ask a question about the video")
    submit_button = st.form_submit_button(label='Send')
    if submit_button and user_question:
        st.session_state.chat_history.insert(0, {"user": user_question, "bot": "Fetching answer..."})
        answer = query_transcripts(user_question)  # Fetch answer from Flask API
        if "Error" in answer:  # Fallback to dummy reply in case of error
            answer = get_dummy_answer(user_question)
        st.session_state.chat_history[0]["bot"] = answer

# Display chat history with most recent chat at the top
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.write("---")
