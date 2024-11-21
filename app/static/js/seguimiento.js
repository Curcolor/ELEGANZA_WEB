document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript cargado'); // Verificar que el script se carga

    const formSeguimiento = document.getElementById('form-seguimiento');
    const mensajeContainer = document.getElementById('mensaje-container');
    const pedidoInfo = document.getElementById('pedido-info');

    if (!formSeguimiento || !mensajeContainer || !pedidoInfo) {
        console.error('No se encontraron elementos necesarios');
        return;
    }

    formSeguimiento.addEventListener('submit', function(e) {
        e.preventDefault();
        console.log('Formulario enviado'); // Debug

        const codigoInput = document.getElementById('codigo-seguimiento');
        const codigo = codigoInput.value.trim();

        // Mostrar mensaje inmediatamente para verificar que funciona
        const mensajeDiv = document.createElement('div');
        mensajeDiv.className = 'alerta alerta-error';
        mensajeDiv.style.backgroundColor = '#fee2e2';
        mensajeDiv.style.color = '#dc2626';
        mensajeDiv.style.padding = '1rem';
        mensajeDiv.style.margin = '1rem 0';
        mensajeDiv.style.borderRadius = '8px';
        mensajeDiv.style.textAlign = 'center';
        mensajeDiv.style.border = '1px solid #fecaca';

        if (!codigo.match(/^P-\d{6}$/)) {
            mensajeDiv.textContent = 'Formato inválido. Debe ser P-XXXXXX (donde X son números)';
        } else {
            mensajeDiv.textContent = 'Buscando pedido...';
            mensajeDiv.style.backgroundColor = '#dcfce7';
            mensajeDiv.style.color = '#16a34a';
            mensajeDiv.style.border = '1px solid #bbf7d0';
        }

        // Limpiar mensajes anteriores
        mensajeContainer.innerHTML = '';
        
        // Agregar nuevo mensaje
        mensajeContainer.appendChild(mensajeDiv);
        
        console.log('Mensaje agregado al contenedor'); // Debug
    });
}); 