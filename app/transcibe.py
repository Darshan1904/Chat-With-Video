# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

from dotenv import load_dotenv
import os
import assemblyai as aai
from . import summarize
# Replace with your API key
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

# URL of the file to transcribe

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()
def transcribe_summarise(fileUrl):
    transcript = transcriber.transcribe(fileUrl)
    if transcript.status == aai.TranscriptStatus.error:
        return {'Error':transcript.error}
    else:
        text = transcript.text 
        summary = summarize.summarize_text(text)
        return {"summary" : summary}

# print(transcribe_summarise('https://github.com/AssemblyAI-Community/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3'))