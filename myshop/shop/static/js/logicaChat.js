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

function esbribirMensaje(mensaje, buton) {
    const nuevoMensaje = document.createElement('div')
    nuevoMensaje.classList.add('mensaje')
    const parrafo = document.createElement('p')
    if (buton) {
        const parte1 = mensaje.split('*PATH:')[0]
        const parte2 = mensaje.split(':PATH*')[1]
        parrafo.innerText = parte1
        nuevoMensaje.appendChild(parrafo)
        const btn = document.createElement('button')
        btn.classList.add('btnVerProducto')
        btn.innerText = 'Ver'
        btn.addEventListener('click', () => {
            window.open(`${window.location.protocol}//${window.location.host}/${mensaje.split('*PATH:')[1].split(':PATH*')[0]}`, '_blank')
        })
        nuevoMensaje.appendChild(btn)
        if(parte2 !== undefined){
            const parrafo2 = document.createElement('p')
            parrafo2.innerText = parte2
            nuevoMensaje.appendChild(parrafo2)
        }
    }else{
        parrafo.innerText = mensaje
        nuevoMensaje.appendChild(parrafo)
    }
    seccionMensajes.appendChild(nuevoMensaje)
    cuerpoChat.scrollTo(0, cuerpoChat.scrollHeight)
}

formChat.addEventListener('submit', (e) => {
    e.preventDefault()
    const mensaje = formChat.querySelector('input').value
    if (mensaje.trim().length > 0) {
        // recuperamos los mensajes del chatbot
        let mensajesChatBot = document.querySelectorAll('.mensaje')
        mensajesChatBot = Array.from(mensajesChatBot).map((mensaje, inidice) => {
            if(inidice === 0) return mensaje.innerText
            let parrafos = mensaje.querySelectorAll('p')
            parrafos = Array.from(parrafos).map(parrafo => parrafo.innerText)
            return parrafos.join('. ')
        })
        // recuperamos los mensajes del usuario
        let mensajesUsuario = document.querySelectorAll('.mensajeUsuario')
        mensajesUsuario = Array.from(mensajesUsuario).map(mensaje => mensaje.innerText)
        const nuevoMensaje = document.createElement('div')
        nuevoMensaje.classList.add('mensajeUsuario')
        nuevoMensaje.innerText = mensaje
        seccionMensajes.appendChild(nuevoMensaje)
        escribiendo.classList.add('activo')
        cuerpoChat.scrollTo(0, cuerpoChat.scrollHeight)
        fetch('https://api-chat-deploy-dev-kecs.2.us-1.fl0.io/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ mensaje: mensaje, mensajesChatBot: mensajesChatBot, mensajesUsuario: mensajesUsuario })
        }).then(res => res.json())
            .then(res => {
                let tieneBoton = res.respuesta.includes('*PATH:')
                esbribirMensaje(res.respuesta, tieneBoton)
            }).catch(err => {
                console.log(err); esbribirMensaje('Lo siento, ocurrió un error, intenta más tarde. Nos disculpamos por las molestias.')
            }).finally(() => {
                escribiendo.classList.remove('activo')
            })
        formChat.querySelector('input').value = ''
    }
})