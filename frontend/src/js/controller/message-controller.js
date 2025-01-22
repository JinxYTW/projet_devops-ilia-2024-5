import { MessageService } from '../services/message-service.js';
import { MessageView } from '../view/message-view.js';

export class MessageController {
    constructor() {
        this.service = new MessageService('https://api.example.com'); // J'ai pas trouvé l'url de l'API
        this.view = new MessageView();
        //Je sais pas trop comment on passe les id/token ou atre donc pour l'instant je suis parti du principe que l'on fait passé par URL
        const params = new URLSearchParams(window.location.search);
        this.currentUser = 'user1'; // J'imagine que c'est l'ID de l'utilisateur courant,genre récupéré après connexion
        this.contactUser = params.get('contactUser'); // J'imagine que c'est l'ID de l'utilisateur avec qui on discute récupéré après appui sur la liste des gens dispo dans la liste des mp's
        
    }

    async init() {
        try {
            const messages = await this.service.getMessages(this.currentUser, this.contactUser);
            this.view.renderMessages(messages);
        } catch (error) {
            console.error(error);
        }

        this.view.onSendMessage(async (content) => {
            if (content.trim() === '') return;

            try {
                await this.service.sendMessage(this.currentUser, this.contactUser, content);
                const messages = await this.service.getMessages(this.currentUser, this.contactUser);
                this.view.renderMessages(messages);
                this.view.clearMessageInput();
            } catch (error) {
                console.error(error);
            }
        });
    }

    async markAsRead(messageId) {
        try {
            await this.service.markMessageAsRead(messageId);
            console.log(`Message ${messageId} lu.`);
        } catch (error) {
            console.error('Une erreur est survenue lors de la lecture', error);
        }
    }
    
    async deleteMessage(messageId) {
        try {
            await this.service.deleteMessage(messageId);
            console.log(`Message ${messageId} supprimé.`);
            const messages = await this.service.getMessages(this.currentUser, this.contactUser);
            this.view.renderMessages(messages);
        } catch (error) {
            console.error('Une erreur est survenue lors de la suppression', error);
        }
    }
    
}
