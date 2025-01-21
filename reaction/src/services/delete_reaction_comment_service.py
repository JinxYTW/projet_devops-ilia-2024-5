import json
from db.redis_client import get_redis_client

def delete_reaction_comment(comment_id, reaction_id):
    client = get_redis_client()
    reaction_key = f"comment:{comment_id}:reactions"

    # Retrieve the reaction data before deleting
    reaction_data_json = client.hget(reaction_key, reaction_id)
    if reaction_data_json:
        reaction_data = json.loads(reaction_data_json)
        
        # Delete the specified reaction
        client.hdel(reaction_key, reaction_id)
        
        # Update the reactions count in reactions_stat
        reactions_stat_key = f"comment:{comment_id}:reactions_stat"
        client.hincrby(reactions_stat_key, reaction_data['reaction'], -1)
        return True  # Reaction successfully deleted

    return False  # Reaction not found
