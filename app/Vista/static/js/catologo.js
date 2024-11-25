document.querySelectorAll('.btn-agregar-carrito').forEach(button => {
    button.addEventListener('click', async function() {
        const productoId = this.dataset.productoId;
        try {
            const response = await fetch('/api/carrito', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id_usuario: 1, // Esto debería venir de la sesión del usuario
                    id_producto: productoId,
                    cantidad: 1
                })
            });
            
            const data = await response.json();
            if (data.success) {
                // Actualizar el contador del carrito
                document.querySelector('.carrito-contador').textContent = data.total_items;
                // Mostrar mensaje de éxito
                alert('Producto agregado al carrito');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error al agregar al carrito');
        }
    });
});