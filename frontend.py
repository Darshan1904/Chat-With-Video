# import streamlit as st
# from pytube import YouTube
# from pytube.cli import on_progress

# def fetch_transcripts(video_url):
#     try:
#         yt = YouTube(video_url, on_progress_callback=on_progress)
#         caption = yt.captions.get_by_language_code('en')
#         if caption:
#             return caption.generate_srt_captions()
#         else:
#             return "No transcripts available for this video."
#     except Exception as e:
#         return f"An error occurred: {e}"

# st.title("YouTube Video and Transcripts Viewer")

# st.sidebar.header("Upload or Provide Link")
# input_type = st.sidebar.radio("Choose input type", ["Provide link", "Upload from computer"])

# if input_type == "Provide link":
#     video_url = st.sidebar.text_input("Enter YouTube URL")
#     if st.sidebar.button("Fetch Video"):
#         if video_url:
#             try:
#                 yt = YouTube(video_url)
#                 st.video(video_url)
#                 transcripts = fetch_transcripts(video_url)
#                 st.subheader("Transcripts")
#                 st.text_area("Transcripts", transcripts, height=300)
#             except Exception as e:
#                 st.error(f"Failed to load video: {e}")
#         else:
#             st.warning("Please enter a valid YouTube URL.")

# elif input_type == "Upload from computer":
#     uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
#     if uploaded_file:
#         st.video(uploaded_file)
#         st.subheader("Transcripts")
#         st.text_area("Transcripts", "Upload functionality does not support transcripts yet.", height=300)

# import streamlit as st
# from pytube import YouTube
# from pytube.cli import on_progress
# import random

# # Function to fetch transcripts
# def fetch_transcripts(video_url):
#     try:
#         yt = YouTube(video_url, on_progress_callback=on_progress)
#         caption = yt.captions.get_by_language_code('en')
#         if caption:
#             return caption.generate_srt_captions()
#         else:
#             return "No transcripts available for this video."
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Dummy replies array
# dummy_replies = [
#     "That's a great question! The answer is quite simple...",
#     "I believe the video explains this point around the 5-minute mark.",
#     "This concept is explained in detail in the transcripts.",
#     "Please refer to the section where the speaker talks about this topic.",
#     "I'm not sure, but let me look into it and get back to you.",
#     "This is a bit complex, but I'll try to simplify it for you..."
# ]

# # Function to get a dummy answer
# def get_dummy_answer(question):
#     return random.choice(dummy_replies)

# st.title("YouTube Video and Transcripts Viewer")

# st.sidebar.header("Upload or Provide Link")
# input_type = st.sidebar.radio("Choose input type", ["Provide link", "Upload from computer"])

# if input_type == "Provide link":
#     video_url = st.sidebar.text_input("Enter YouTube URL")
#     if st.sidebar.button("Fetch Video"):
#         if video_url:
#             try:
#                 yt = YouTube(video_url)
#                 st.video(video_url)
#                 transcripts = fetch_transcripts(video_url)
#                 st.subheader("Transcripts")
#                 st.text_area("Transcripts", transcripts, height=300)
#             except Exception as e:
#                 st.error(f"Failed to load video: {e}")
#         else:
#             st.warning("Please enter a valid YouTube URL.")

# elif input_type == "Upload from computer":
#     uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
#     if uploaded_file:
#         st.video(uploaded_file)
#         st.subheader("Transcripts")
#         st.text_area("Transcripts", "Upload functionality does not support transcripts yet.", height=300)

# # Chat section
# st.subheader("Chat with Video")

# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# user_question = st.text_input("Ask a question about the video")
# if st.button("Send"):
#     if user_question:
#         st.session_state.chat_history.insert(0, {"user": user_question, "bot": "Fetching answer..."})
#         answer = get_dummy_answer(user_question)
#         st.session_state.chat_history[0]["bot"] = answer
#     else:
#         st.warning("Please enter a question.")

# # Display chat history with most recent chat at the top
# for chat in st.session_state.chat_history:
#     st.markdown(f"**You:** {chat['user']}")
#     st.markdown(f"**Bot:** {chat['bot']}")
#     st.write("---")

import streamlit as st
from pytube import YouTube
from pytube.cli import on_progress
import random

# Function to fetch transcripts
def fetch_transcripts(video_url):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        caption = yt.captions.get_by_language_code('en')
        if caption:
            return caption.generate_srt_captions()
        else:
            return "No transcripts available for this video."
    except Exception as e:
        return f"An error occurred: {e}"

# Dummy replies array
dummy_replies = [
    "That's a great question! The answer is quite simple...",
    "I believe the video explains this point around the 5-minute mark.",
    "This concept is explained in detail in the transcripts.",
    "Please refer to the section where the speaker talks about this topic.",
    "I'm not sure, but let me look into it and get back to you.",
    "This is a bit complex, but I'll try to simplify it for you..."
]

# Function to get a dummy answer
def get_dummy_answer(question):
    return random.choice(dummy_replies)

st.title("YouTube Video and Transcripts Viewer")

st.sidebar.header("Upload or Provide Link")
input_type = st.sidebar.radio("Choose input type", ["Provide link", "Upload from computer"])

if input_type == "Provide link":
    video_url = st.sidebar.text_input("Enter YouTube URL")
    fetch_video_button = st.sidebar.button("Fetch Video")
    if fetch_video_button and video_url:
        try:
            yt = YouTube(video_url)
            st.session_state.video_url = video_url
            st.session_state.transcripts = fetch_transcripts(video_url)
        except Exception as e:
            st.error(f"Failed to load video: {e}")
elif input_type == "Upload from computer":
    uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if uploaded_file:
        st.session_state.video_file = uploaded_file
        st.session_state.transcripts = "Upload functionality does not support transcripts yet."

# Display video and transcripts if available
if 'video_url' in st.session_state:
    st.video(st.session_state.video_url)
if 'video_file' in st.session_state:
    st.video(st.session_state.video_file)
if 'transcripts' in st.session_state:
    st.subheader("Transcripts")
    st.text_area("Transcripts", st.session_state.transcripts, height=300)

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
        answer = get_dummy_answer(user_question)
        st.session_state.chat_history[0]["bot"] = answer

# Display chat history with most recent chat at the top
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.write("---")
