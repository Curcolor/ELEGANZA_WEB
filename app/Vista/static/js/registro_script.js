document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('formularioRegistro').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const datos = {
            nombre: document.getElementById('nombre').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value
        };

        try {
            const response = await fetch('/usuarios', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });

            const resultado = await response.json();

            if (response.ok) {
                document.getElementById('mensaje').innerHTML = '¡Registro exitoso!';
                document.getElementById('formularioRegistro').reset();
                setTimeout(() => {
                    window.location.href = '/login';
                }, 1500);
            } else {
                document.getElementById('mensaje').innerHTML = `Error: ${resultado.error}`;
            }
        } catch (error) {
            console.error('Error:', error);
            document.getElementById('mensaje').innerHTML = 'Error al registrar usuario';
        }
    });
});