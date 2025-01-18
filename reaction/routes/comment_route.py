from flask import Blueprint, request, jsonify
from services.comment_service import add_comment

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/tweets/<tweet_id>/comments', methods=['POST'])
def create_comment(tweet_id):
    data = request.get_json()
    result = add_comment(tweet_id, data)
    return jsonify(result), 201
