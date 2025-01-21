from database import get_messages  
 
messages = get_messages()

def mark_as_read(message_id):
    """
    Marque un message comme lu
    """
    if message_id in messages:
        messages[message_id]["isRead"] = True
        return True
    return False