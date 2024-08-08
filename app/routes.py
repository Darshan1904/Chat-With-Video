from flask import Blueprint, request, jsonify
from . import query
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
    response = query.transcribe_and_store(videoURL)  # Ensure this function is defined somewhere
    # print(response,type(response))
    return jsonify(response)


@bp.route('/query',methods=['POST'])
def q():
    data = request.json
    qu = data.get('query')
    if not qu : return jsonify({'error' : 'Please enter a query'})
    response = query.query_transcript(qu)
    return jsonify(response)
