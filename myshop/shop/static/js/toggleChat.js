const chatButton = document.getElementById('chat-button');
const chatContainer = document.getElementById('chat-container');
// Función para alternar la visibilidad del chat
function toggleChat() {
    if (chatContainer.style.display === 'none' || chatContainer.style.display === '') {
        chatContainer.style.display = 'block';
        chatButton.textContent = 'Cerrar Chat';
    } else {
        chatContainer.style.display = 'none';
        chatButton.textContent = 'Abrir Chat';
    }
}
chatButton.addEventListener('click', toggleChat);