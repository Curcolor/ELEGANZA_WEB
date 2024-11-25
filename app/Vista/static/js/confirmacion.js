document.addEventListener('DOMContentLoaded', function() {
    console.log('Buscando datos del pedido...'); // Debug log
    
    // Obtener los datos del pedido del localStorage
    const datosPedidoStr = localStorage.getItem('datosPedido');
    console.log('Datos encontrados:', datosPedidoStr); // Debug log
    
    if (datosPedidoStr) {
        try {
            const datosPedido = JSON.parse(datosPedidoStr);
            console.log('Datos parseados:', datosPedido); // Debug log
            
            // Actualizar los elementos del DOM
            const elementos = {
                'numero-pedido': datosPedido.id,
                'codigo-seguimiento': datosPedido.codigo_seguimiento,
                'fecha-pedido': datosPedido.fecha,
                'total-pedido': `$${datosPedido.total}`,
                'estado-pedido': datosPedido.estado
            };
            
            // Actualizar cada elemento si existe
            Object.entries(elementos).forEach(([id, valor]) => {
                const elemento = document.getElementById(id);
                if (elemento && valor) {
                    elemento.textContent = valor;
                    if (id === 'estado-pedido') {
                        elemento.setAttribute('data-estado', valor.toLowerCase());
                    }
                }
            });
            
            // Limpiar localStorage después de usar los datos
            localStorage.removeItem('datosPedido');
            
        } catch (error) {
            console.error('Error al parsear los datos del pedido:', error);
            mostrarErrorDeCarga();
        }
    } else {
        console.log('No hay datos de pedido en localStorage');
        mostrarErrorDeCarga();
    }
});

function mostrarErrorDeCarga() {
    const elementos = ['numero-pedido', 'codigo-seguimiento', 'fecha-pedido', 'total-pedido', 'estado-pedido'];
    elementos.forEach(id => {
        const elemento = document.getElementById(id);
        if (elemento) {
            elemento.textContent = 'No disponible';
        }
    });
} 