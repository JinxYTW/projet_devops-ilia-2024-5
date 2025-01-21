from database import get_messages  
 
messages, message_counter = get_messages()

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