from db.redis_client import get_redis_client

def delete_comment_by_id(comment_id):
    """
    Supprime un commentaire en utilisant son ID depuis Redis.
    """
    client = get_redis_client()
    
    # Récupérer les commentaires depuis Redis
    comments = client.get('comments')
    
    if comments is None:
        # Aucun commentaire dans Redis
        return False
    else:
        # Convertir les données récupérées en une liste d'objets Python
        comments = eval(comments)
        
        # Trouver le commentaire à supprimer
        comment_to_delete = next((comment for comment in comments if comment['id'] == comment_id), None)
        
        if comment_to_delete:
            # Supprimer le commentaire trouvé
            comments = [comment for comment in comments if comment['id'] != comment_id]
            
            # Mettre à jour les données dans Redis
            client.set('comments', str(comments))
            return True
    
    # Si le commentaire n'a pas été trouvé
    return False
