from flask import Blueprint, request, jsonify
# from .gemini_client import query_gemini

bp = Blueprint('main', __name__)

@bp.route("/hello",methods=["GET"])
def hello():
    return "hello world"


# @bp.route('/ask', methods=['POST'])
# def ask_gemini():
#     data = request.json
#     question = data.get('question')
    
#     if not question:
#         return jsonify({'error': 'No question provided'}), 400

#     response = query_gemini(question)
    
#     return jsonify(response)

