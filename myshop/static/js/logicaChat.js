const contenedorChat = document.getElementById('contenedorChat')
const btnMostrarChat = document.getElementById('btnChat')
const btnCerrarChat = document.getElementById('cabezaChat').querySelector('svg')
const seccionMensajes = document.getElementById('seccionMensajes')
const formChat = document.getElementById('formularioChat')
const escribiendo = document.getElementById('chatBotEscribiendo')
const cuerpoChat = document.getElementById('cuerpoChat')

btnMostrarChat.addEventListener('click', () => {
    contenedorChat.querySelectorAll('footer')[1].classList.remove('activo')
    contenedorChat.querySelector('header').classList.add('activo')
    formChat.querySelector('input').focus()
})

btnCerrarChat.addEventListener('click', () => {
    contenedorChat.querySelectorAll('footer')[1].classList.add('activo')
    contenedorChat.querySelector('header').classList.remove('activo')
    seccionMensajes.innerHTML = ''
    esbribirMensaje('Hola, ¿en qué puedo ayudarte?')
})

function esbribirMensaje(mensaje) {
    const nuevoMensaje = document.createElement('div')
    nuevoMensaje.classList.add('mensaje')
    nuevoMensaje.innerText = mensaje
    seccionMensajes.appendChild(nuevoMensaje)
    cuerpoChat.scrollTo(0, cuerpoChat.scrollHeight)
}

formChat.addEventListener('submit', (e) => {
    e.preventDefault()
    const mensaje = formChat.querySelector('input').value
    if (mensaje.trim().length > 0) {
        const nuevoMensaje = document.createElement('div')
        nuevoMensaje.classList.add('mensajeUsuario')
        nuevoMensaje.innerText = mensaje
        seccionMensajes.appendChild(nuevoMensaje)
        escribiendo.classList.add('activo')
        cuerpoChat.scrollTo(0, cuerpoChat.scrollHeight)
        fetch('https://api-chat-deploy-2s7l-dev.fl0.io/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ mensaje: mensaje })
        }).then(res => res.json())
            .then(res => {
                esbribirMensaje(res.text)
            }).catch(err => {
                console.log(err); esbribirMensaje('Lo siento, ocurrió un error, intenta más tarde. Nos disculpamos por las molestias.')
            }).finally(() => {
                escribiendo.classList.remove('activo')
            })
        formChat.querySelector('input').value = ''
    }
})