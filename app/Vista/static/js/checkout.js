const pasos = ['direccion', 'envio', 'pago'];
        let pasoActual = 'direccion';

        function actualizarPasos() {
            pasos.forEach(paso => {
                const elemento = document.getElementById(`paso-${paso}`);
                const formulario = document.getElementById(`form-${paso}`);
                
                if (paso === pasoActual) {
                    elemento.classList.add('activo');
                    formulario.classList.remove('hidden');
                } else {
                    elemento.classList.remove('activo');
                    formulario.classList.add('hidden');
                }
            });
        }

        function actualizarContadorCarrito() {
            fetch('/obtener-total-carrito')
                .then(response => response.json())
                .then(data => {
                    const contador = document.querySelector('.carrito-contador');
                    if (contador) {
                        contador.textContent = data.total;
                        contador.style.display = data.total > 0 ? 'block' : 'none';
                    }
                })
                .catch(error => console.error('Error al actualizar contador:', error));
        }

        function mostrarDireccion() {
            pasoActual = 'direccion';
            actualizarPasos();
        }

        function mostrarEnvio() {
            pasoActual = 'envio';
            actualizarPasos();
        }

        function mostrarPago() {
            pasoActual = 'pago';
            actualizarPasos();
        }

        // Event Listeners para los formularios
        document.getElementById('direccion-form').addEventListener('submit', function(e) {
            e.preventDefault();
            mostrarEnvio();
        });

        document.getElementById('envio-form').addEventListener('submit', function(e) {
            e.preventDefault();
            mostrarPago();
        });

        document.getElementById('pago-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const datosPedido = {
                id_usuario: userId,
                total: total,
                direccion_envio: document.getElementById('calle').value,
                metodo_pago: 'tarjeta'
            };

            fetch('/confirmar_compra', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datosPedido)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Datos del pedido recibidos:', data.pedido); // Debug log
                    
                    // Guardar los datos completos del pedido
                    const pedidoParaGuardar = {
                        id: data.pedido.id,
                        codigo_seguimiento: data.pedido.codigo_seguimiento,
                        fecha: data.pedido.fecha,
                        total: data.pedido.total,
                        estado: data.pedido.estado
                    };
                    
                    // Guardar en localStorage
                    localStorage.setItem('datosPedido', JSON.stringify(pedidoParaGuardar));
                    
                    // Reiniciar contador del carrito
                    const contador = document.querySelector('.carrito-contador');
                    if (contador) {
                        contador.textContent = '0';
                        contador.style.display = 'none';
                    }
                    
                    // Redirigir a la página de confirmación
                    window.location.href = `/confirmacion/${data.pedido.id}`;
                } else {
                    alert('Error al procesar el pedido: ' + data.mensaje);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al procesar el pedido: ' + error);
            });
        });

        