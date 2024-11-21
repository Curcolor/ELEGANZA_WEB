function actualizarContadorCarrito() {
    fetch('/obtener-total-carrito')
        .then(response => response.json())
        .then(data => {
            const contador = document.querySelector('.carrito-contador');
            contador.textContent = data.total;
            contador.style.display = data.total > 0 ? 'block' : 'none';
        });
}

document.addEventListener('DOMContentLoaded', function() {
    // Interceptar todos los formularios de agregar al carrito
    document.querySelectorAll('.form-agregar-carrito').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    actualizarContadorCarrito();
                    
                    // Crear notificación flotante
                    const notification = document.createElement('div');
                    notification.className = 'notification';
                    notification.innerHTML = `
                        <p>¡Producto agregado al carrito!</p>
                        <div class="notification-buttons">
                            <button onclick="window.location.href='${window.location.pathname}'">Seguir comprando</button>
                            <button onclick="window.location.href='/carrito'" class="btn-primary">Ir al carrito</button>
                        </div>
                    `;
                    
                    document.body.appendChild(notification);
                    
                    // Remover la notificación después de 5 segundos
                    setTimeout(() => {
                        notification.remove();
                    }, 5000);
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al agregar al carrito');
            });
        });
    });
    
    actualizarContadorCarrito();
}); 