from db.redis_client import get_redis_client

def get_reaction_stats(comment_id):
    client = get_redis_client()
    reaction_key = f"comment:{comment_id}:reactions"
    
    reactions = client.hgetall(reaction_key)  # Hash qui contient les types de réactions et leurs comptes
    
    # Si aucune réaction n'est trouvée, renvoie un dictionnaire vide
    if not reactions:
        return {"like": 0, "love": 0, "sad": 0}  # Exemple, adapte les types de réactions
    
    # Convertir les données binaires de Redis en dictionnaire avec des entiers
    reaction_stats = {reaction.decode(): int(count) for reaction, count in reactions.items()}
    
    return reaction_stats


