# Pour l'instant on simule un stockage des messages, nicopyright avance sur le stockage avec Redis en parallele
messages = {}
message_counter = 1

def send_message(sender, receiver, content):
    """
    Envoie un nouveau message.
    """
    global messages, message_counter
    message_id = str(message_counter)
    messages[message_id] = {
        "sender": sender,
        "receiver": receiver,
        "content": content,
        "isRead": False
    }
    message_counter += 1
    return message_id