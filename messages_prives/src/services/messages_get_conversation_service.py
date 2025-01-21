# Pour l'instant on simule un stockage des messages, nicopyright avance sur le stockage avec Redis en parallele
messages = {}
message_counter = 1

def get_messages(user1, user2):
    """
    Récupère les messages entre deux users
    """
    return [
        {"id": msg_id, **msg}
        for msg_id, msg in messages.items()
        if (msg["sender"] == user1 and msg["receiver"] == user2) or
           (msg["sender"] == user2 and msg["receiver"] == user1)
    ]