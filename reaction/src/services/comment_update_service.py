from db.redis_client import get_redis_client

def update_comment(comment_id, data):
    """
    Modifie un commentaire existant.
    """
    client = get_redis_client()
    
    # Parcourir toutes les clés de commentaires
    all_comment_keys = client.keys("comments:*")
    
    for key in all_comment_keys:
        comments = client.lrange(key, 0, -1)
        for idx, comment in enumerate(comments):
            comment_dict = eval(comment.decode())  # Convertir la chaîne en dictionnaire
            if comment_dict["commentId"] == comment_id:
                # Mettre à jour le contenu du commentaire
                comment_dict["content"] = data["content"]
                client.lset(key, idx, str(comment_dict))  # Mettre à jour Redis
                return {"message": "Comment updated successfully", "commentId": comment_id}
    
    return {"message": "Comment not found"}, 404
