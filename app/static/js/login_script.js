document.addEventListener('DOMContentLoaded', () => {
    const mensajeElement = document.getElementById('mensaje');

    const mostrarMensaje = (mensaje, tipo) => {
        mensajeElement.textContent = mensaje;
        mensajeElement.className = tipo;
        mensajeElement.style.display = 'block';
    };

    document.getElementById('formularioLogin').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const datos = {
            email: document.getElementById('email').value,
            password: document.getElementById('password').value
        };

        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });

            const resultado = await response.json();

            if (response.ok) {
                mostrarMensaje('¡Inicio de sesión exitoso!', 'success');
                // Guardamos la información del usuario en localStorage
                localStorage.setItem('usuario', JSON.stringify(resultado.usuario));
                
                // Redirigimos a la página de cuenta después de un breve delay
                setTimeout(() => {
                    window.location.href = CUENTA_URL;
                }, 1500);
            } else {
                mostrarMensaje(`Error: ${resultado.mensaje}`, 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            mostrarMensaje('Error al iniciar sesión', 'error');
        }
    });
}); 