document.addEventListener('DOMContentLoaded', function() {
    const formPerfil = document.getElementById('form-perfil');
    
    if (formPerfil) {
        formPerfil.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const datos = {
                nombre: formPerfil.querySelector('input[name="nombre"]').value
            };

            try {
                const response = await fetch(ACTUALIZAR_PERFIL_URL, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(datos)
                });

                const resultado = await response.json();

                if (response.ok) {
                    alert('Perfil actualizado exitosamente');
                    // Actualizar el nombre en el menú lateral
                    document.querySelector('.perfil-info h3').textContent = datos.nombre;
                } else {
                    alert(resultado.mensaje || 'Error al actualizar el perfil');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error al actualizar el perfil');
            }
        });
    }

    // Manejar cierre de sesión
    const btnCerrarSesion = document.querySelector('.cerrar-sesion');
    if (btnCerrarSesion) {
        btnCerrarSesion.addEventListener('click', async function(e) {
            e.preventDefault();
            try {
                const response = await fetch('/logout');
                if (response.ok) {
                    window.location.href = '/login';
                }
            } catch (error) {
                console.error('Error al cerrar sesión:', error);
            }
        });
    }
}); 