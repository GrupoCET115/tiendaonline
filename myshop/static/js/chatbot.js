 const chatOutput = document.getElementById('chat-output');
 const userInput = document.getElementById('user-input');
 const sendButton = document.getElementById('send-button');
 // Respuestas del chatbot (puedes personalizarlas)
 const botResponses = ["¡Hola! ¿En qué puedo ayudarte hoy?", "¿Qué producto estás buscando?", "Puedes encontrar productos en nuestra tienda en línea.", "¿Necesitas ayuda con algo más?"];
 // Función para agregar mensajes al chat
 function addMessage(message, isUser = false) {
     const messageElement = document.createElement('div');
     messageElement.classList.add(isUser ? 'user-message' : 'bot-message');
     messageElement.textContent = message;
     chatOutput.appendChild(messageElement);
 }
 // Función para manejar la entrada del usuario
 function handleUserInput() {
     const userMessage = userInput.value;
     if (userMessage.trim() === "") return;
     addMessage(userMessage, true);
     userInput.value = ""; // Limpiar el campo de entrada
     // Simular una respuesta del chatbot (puedes reemplazar esto con lógica real)
     const botResponse = botResponses[Math.floor(Math.random() * botResponses.length)];
     setTimeout(() => {
         addMessage(botResponse);
     }, 500);
 }
 // Manejar clic en el botón de enviar
 sendButton.addEventListener('click', handleUserInput);
 // Manejar la tecla "Enter" para enviar
 userInput.addEventListener('keypress', function(event) {
     if (event.key === "Enter") {
         handleUserInput();
     }
 });