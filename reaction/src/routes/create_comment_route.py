from flask import Blueprint, request, jsonify

from services.comment_service import add_comment_to_twwet, add_comment_to_comment

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/tweets/<tweet_id>/comments', methods=['POST'])
def create_comment_tweet(tweet_id):
    data = request.get_json()
    result = add_comment_to_twwet(tweet_id, data)
    return jsonify(result), 201


@comment_bp.route('/comments/<comment_id>/comments', methods=['POST'])
def create_comment_comment(comment_id):
    data = request.get_json()
    result = add_comment_to_comment(comment_id, data)
    return jsonify(result), 201