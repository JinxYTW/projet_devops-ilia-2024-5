export class MessageService {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async sendMessage(sender, receiver, content) {
        const response = await fetch(`${this.baseUrl}/messages`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sender, receiver, content }),
        });

        if (!response.ok) {
            throw new Error('Envoie du message échoué');
        }

        return await response.json();
    }

    async getMessages(user1, user2) {
        const response = await fetch(`${this.baseUrl}/messages/${user1}/${user2}`);
        if (!response.ok) {
            throw new Error('Récupération des messages échouée');
        }
        return await response.json();
    }

    async deleteMessage(messageId) {
        const response = await fetch(`${this.baseUrl}/messages/${messageId}`, {
            method: 'DELETE',
        });
    
        if (!response.ok) {
            throw new Error('Suppression du message échouée');
        }
        return await response.json();
    }
    

    async markMessageAsRead(messageId) {
        const response = await fetch(`${this.baseUrl}/messages/${messageId}`, {
            method: 'PUT',
        });

        if (!response.ok) {
            throw new Error('Marquage du message comme lu échoué');
        }
        return response.json();
    }
}
