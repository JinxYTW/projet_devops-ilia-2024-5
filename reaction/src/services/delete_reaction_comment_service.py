from db.redis_client import get_redis_client

def delete_reaction_comment(comment_id, reaction_id):
    client = get_redis_client()

    # Récupérer les réactions associées au commentaire
    reactions = client.get(f'reactions:{comment_id}')

    if reactions is None:
        raise ValueError("Comment not found")

    # Désérialisation des données
    reactions = eval(reactions)

    # Filtrer pour supprimer la réaction spécifique
    updated_reactions = [r for r in reactions if r["reaction_id"] != reaction_id]

    # Si aucune modification n'est nécessaire
    if len(reactions) == len(updated_reactions):
        raise ValueError("Reaction not found")

    # Mettre à jour les réactions dans Redis
    client.set(f'reactions:{comment_id}', str(updated_reactions))

    return True
