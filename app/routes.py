from flask import Blueprint, request, jsonify
from . import transcibe
bp = Blueprint('main', __name__)

@bp.route("/hello", methods=["GET"])
def hello():
    return "hello world"

@bp.route('/transcribe', methods=['POST'])
def transcribe():
    data = request.json
    videoURL = data.get('videoURL')
    # print(videoURL)
    if not videoURL:
        return jsonify({'error': "No video URL provided"}), 400
    response = transcibe.transcribe_summarise(videoURL)  # Ensure this function is defined somewhere
    # print(response,type(response))
    return jsonify(response)
