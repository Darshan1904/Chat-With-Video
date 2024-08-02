import streamlit as st
from pytube import YouTube
from pytube.cli import on_progress

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

st.title("YouTube Video and Transcripts Viewer")

st.sidebar.header("Upload or Provide Link")
input_type = st.sidebar.radio("Choose input type", ["Provide link", "Upload from computer"])

if input_type == "Provide link":
    video_url = st.sidebar.text_input("Enter YouTube URL")
    if st.sidebar.button("Fetch Video"):
        if video_url:
            try:
                yt = YouTube(video_url)
                st.video(video_url)
                transcripts = fetch_transcripts(video_url)
                st.subheader("Transcripts")
                st.text_area("Transcripts", transcripts, height=300)
            except Exception as e:
                st.error(f"Failed to load video: {e}")
        else:
            st.warning("Please enter a valid YouTube URL.")

elif input_type == "Upload from computer":
    uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if uploaded_file:
        st.video(uploaded_file)
        st.subheader("Transcripts")
        st.text_area("Transcripts", "Upload functionality does not support transcripts yet.", height=300)
