from db.redis_client import get_redis_client

def delete_comment_by_id(comment_id):
    """
    Supprime un commentaire spécifique en utilisant son ID dans Redis.
    """
    client = get_redis_client()

    # Récupérer tous les commentaires
    all_comment_keys = client.keys("comments:*")
    
    for key in all_comment_keys:
        comments = client.lrange(key, 0, -1)
        for idx, comment in enumerate(comments):
            comment_dict = eval(comment.decode())  # Convertir la chaîne en dictionnaire
            if comment_dict["comment_id"] == comment_id:
                # Mettre à jour le contenu du commentaire
                client.lrem(key, 0, comment)
                return True

    # Si le commentaire n'est pas trouvé
    return False
