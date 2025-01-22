export class MessageView {
    constructor() {
        this.chatArea = document.querySelector('.chat-area');
        this.messageInput = document.querySelector('.footer input');
        this.sendButton = document.querySelector('.footer button[title="Envoyer"]');
    }

    renderMessages(messages) {
        this.chatArea.innerHTML = '';
        messages.forEach((msg) => {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('chat-message', msg.sender === 'me' ? 'sent' : 'received');
            messageDiv.innerHTML = `<div class="message">${msg.content}</div>`;
            this.chatArea.appendChild(messageDiv);
        });
    }

    getMessageInput() {
        return this.messageInput.value;
    }

    clearMessageInput() {
        this.messageInput.value = '';
    }

    onSendMessage(callback) {
        this.sendButton.addEventListener('click', () => {
            const content = this.getMessageInput();
            callback(content);
        });
    }
}
