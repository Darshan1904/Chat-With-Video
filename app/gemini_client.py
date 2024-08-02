# import requests
# from .config import Config

# def query_gemini(question):
#     headers = {
#         'Authorization': f'Bearer {Config.GEMINI_API_KEY}',
#         'Content-Type': 'application/json'
#     }
#     payload = {
#         'question': question
#     }
#     response = requests.post(Config.GEMINI_API_URL, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {'error': 'Failed to get response from Gemini'}, response.status_code
