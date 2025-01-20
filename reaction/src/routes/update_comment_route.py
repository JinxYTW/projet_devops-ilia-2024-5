from flask import Blueprint, request, jsonify
from services.comment_update_service import update_comment

update_comment_bp = Blueprint('update_comment_bp', __name__)

@update_comment_bp.route('/comments/<comment_id>', methods=['PUT'])
def modify_comment(comment_id):
    """
    Permet à un utilisateur de modifier son commentaire.
    """
    data = request.get_json()

    # Vérifier que le champ "content" est présent
    if "content" not in data:
        return jsonify({"message": "Content is required"}), 400

    # Appeler le service de mise à jour
    result = update_comment(comment_id, data)
    
    # Retourner la réponse appropriée
    return jsonify(result), 200 if result.get("message") == "Comment updated successfully" else 404
