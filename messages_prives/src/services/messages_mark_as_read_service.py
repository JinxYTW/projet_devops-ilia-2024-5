
# Pour l'instant on simule un stockage des messages, nicopyright avance sur le stockage avec Redis en parallele
messages = {}
message_counter = 1

def mark_as_read(message_id):
    """
    Marque un message comme lu
    """
    if message_id in messages:
        messages[message_id]["isRead"] = True
        return True
    return False