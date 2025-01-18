from db.redis_client import get_redis_client
import uuid


def add_comment(tweet_id, data):
    client = get_redis_client()
    comment_id = str(uuid.uuid4())
    comment_data = {
        "commentId": comment_id,
        "userId": data["userId"],
        "content": data["content"]
    }
    client.rpush(f"comments:{tweet_id}", str(comment_data))
    return {"message": "Comment added successfully", "commentId": comment_id}
