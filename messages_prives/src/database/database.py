# Pour l'instant on simule un stockage des messages, nicopyright avance sur le stockage avec Redis en parallele
messages = {}
message_counter = 1

def get_messages():
    """
    Retourne tous les messages
    """
    return messages, message_counter