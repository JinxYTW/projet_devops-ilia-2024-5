from flask import Blueprint, jsonify
from reaction.src.services.delete_reaction_comment_service import delete_reaction_comment

reactions_bp = Blueprint('reactions', __name__)

@reactions_bp.route('/comments/<comment_id>/reactions/<reaction_id>', methods=['DELETE'])
def handle_delete_reaction(comment_id, reaction_id):
    try:
        success = delete_reaction_comment(comment_id, reaction_id)
        if success:
            return jsonify({"message": "Reaction deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
