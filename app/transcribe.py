from youtube_transcript_api import YouTubeTranscriptApi

def videoID(url):
    id = ''
    for char in url[::-1]:
        if char == '=' : 
            break 
        id += char 
    return id[::-1]

def transcribe_func(videoURL):
    try:
        video_id = videoID(videoURL)
        print(f"Attempting to fetch transcript for video ID: {video_id}")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        text = ' '.join([entry['text'] for entry in transcript])
        return {'summary': text}
    except Exception as e:
        print(f"Error fetching transcript: {str(e)}")
        return {'Error': str(e)}

