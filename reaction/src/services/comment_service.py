from db.redis_client import get_redis_client
import uuid
from datetime import datetime

def add_comment_to_twwet(tweet_id, data):
    """
    Ajoute un commentaire pour un tweet spécifique dans Redis.
    """
    client = get_redis_client()
    comment_id = str(uuid.uuid4())
    comment_data = {
        "comment_id": comment_id,
        "user_id": data["user_id"],
        "content": data["content"],
        "created_at": datetime.utcnow().isoformat()  # Ajouter la date de création
    }
    client.rpush(f"comments:{tweet_id}", str(comment_data))
    return {"message": "Comment added successfully", "comment_id": comment_id}



def add_comment_to_comment(tweet_id, data):
    """
    Ajoute un commentaire pour un tweet spécifique dans Redis.
    """
    client = get_redis_client()
    comment_id = str(uuid.uuid4())
    comment_data = {
        "comment_id": comment_id,
        "user_id": data["user_id"],
        "content": data["content"],
        "created_at": datetime.utcnow().isoformat()  # Ajouter la date de création
    }
    client.rpush(f"comments:{tweet_id}", str(comment_data))
    return {"message": "Comment added successfully", "comment_id": comment_id}