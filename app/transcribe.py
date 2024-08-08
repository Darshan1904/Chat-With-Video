from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

# Load environment variables
load_dotenv()

def videoID(url):
    id = ''
    for char in url[::-1]:
        if char == '=' : 
            break 
        id += char 
    return id[::-1]

def transcribe_func(videoURL):
    try:
        # Fetch the transcript
        video_id = videoID(videoURL)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Convert transcript to a single text string
        text = ' '.join([entry['text'] for entry in transcript])
        return {'summary':text}
    except Exception as e:
        return {'Error': str(e)}

