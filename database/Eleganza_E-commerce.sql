-- 1. Tablas independientes (sin foreign keys)
CREATE TABLE `roles` (
    `id_rol` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre_de_rol` VARCHAR(50) NOT NULL
);

CREATE TABLE `tipo_proveedor` (
    `id_tipo_proveedor` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(50) NOT NULL,
    `descripcion` TEXT NULL
);

CREATE TABLE `cupones` (
    `id_cupon` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `codigo` VARCHAR(20) NOT NULL,
    `valor` DECIMAL(10, 2) NOT NULL,
    `solo_vip` BOOLEAN NULL DEFAULT 'DEFAULT TRUE',
    `fecha_inicio` DATETIME NOT NULL,
    `fecha_fin` DATETIME NOT NULL,
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE'
);
ALTER TABLE `cupones` ADD UNIQUE `cupones_codigo_unique`(`codigo`);

-- 2. Tablas con una dependencia
CREATE TABLE `usuarios` (
    `id_usuario` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_rol` INT NOT NULL,
    `nombre` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `es_vip` BOOLEAN NULL DEFAULT 'DEFAULT FALSE',
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE',
    `fecha_registro` DATETIME NULL DEFAULT CURRENT_TIMESTAMP()
);
ALTER TABLE `usuarios` ADD INDEX `usuarios_id_rol_index`(`id_rol`);
ALTER TABLE `usuarios` ADD CONSTRAINT `usuarios_id_rol_foreign` FOREIGN KEY(`id_rol`) REFERENCES `roles`(`id_rol`);

CREATE TABLE `proveedores` (
    `id_proveedor` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_tipo_proveedor` INT NOT NULL,
    `nombre` VARCHAR(100) NOT NULL,
    `direccion` TEXT NULL,
    `telefono` VARCHAR(15) NULL,
    `email` VARCHAR(100) NULL,
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE'
);
ALTER TABLE `proveedores` ADD CONSTRAINT `proveedores_id_tipo_proveedor_foreign` FOREIGN KEY(`id_tipo_proveedor`) REFERENCES `tipo_proveedor`(`id_tipo_proveedor`);

CREATE TABLE `planes_vip` (
    `id_plan` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(50) NOT NULL,
    `descripcion` TEXT NULL,
    `precio` DECIMAL(10, 2) NOT NULL,
    `duracion` INT NOT NULL,
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE',
    `id_cupones` BIGINT NOT NULL
);
ALTER TABLE `planes_vip` ADD INDEX `planes_vip_id_cupones_index`(`id_cupones`);
ALTER TABLE `planes_vip` ADD CONSTRAINT `planes_vip_id_cupones_foreign` FOREIGN KEY(`id_cupones`) REFERENCES `cupones`(`id_cupon`);

-- 3. Tablas con dos o más dependencias
CREATE TABLE `productos` (
    `id_producto` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_proveedor` INT NOT NULL,
    `descripcion` TEXT NULL,
    `precio` DECIMAL(10, 2) NOT NULL,
    `nombre` VARCHAR(100) NOT NULL,
    `stock` INT NOT NULL,
    `imagen` VARCHAR(255) NULL,
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE'
);
ALTER TABLE `productos` ADD CONSTRAINT `productos_id_proveedor_foreign` FOREIGN KEY(`id_proveedor`) REFERENCES `proveedores`(`id_proveedor`);

CREATE TABLE `suscripciones_vip` (
    `id_suscripcion` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_usuario` INT NOT NULL,
    `id_plan` INT NOT NULL,
    `fecha_inicio` DATE NOT NULL,
    `fecha_fin` DATE NOT NULL,
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE'
);
ALTER TABLE `suscripciones_vip` ADD INDEX `suscripciones_vip_id_usuario_index`(`id_usuario`);
ALTER TABLE `suscripciones_vip` ADD INDEX `suscripciones_vip_id_plan_index`(`id_plan`);
ALTER TABLE `suscripciones_vip` ADD CONSTRAINT `suscripciones_vip_id_plan_foreign` FOREIGN KEY(`id_plan`) REFERENCES `planes_vip`(`id_plan`);
ALTER TABLE `suscripciones_vip` ADD CONSTRAINT `suscripciones_vip_id_usuario_foreign` FOREIGN KEY(`id_usuario`) REFERENCES `usuarios`(`id_usuario`);

CREATE TABLE `carritos` (
    `id_carrito` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_usuario` BIGINT NOT NULL,
    `id_producto` BIGINT NOT NULL
);
ALTER TABLE `carritos` ADD UNIQUE `carritos_id_usuario_unique`(`id_usuario`);
ALTER TABLE `carritos` ADD INDEX `carritos_id_producto_index`(`id_producto`);
ALTER TABLE `carritos` ADD CONSTRAINT `carritos_id_usuario_foreign` FOREIGN KEY(`id_usuario`) REFERENCES `usuarios`(`id_usuario`);
ALTER TABLE `carritos` ADD CONSTRAINT `carritos_id_producto_foreign` FOREIGN KEY(`id_producto`) REFERENCES `productos`(`id_producto`);

CREATE TABLE `opiniones` (
    `id_opinion` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_producto` INT NOT NULL,
    `id_usuario` INT NOT NULL,
    `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
    `descripcion` TEXT NULL,
    `calificacion` INT NULL,
    `estado` BOOLEAN NULL DEFAULT 'DEFAULT TRUE'
);
ALTER TABLE `opiniones` ADD INDEX `opiniones_id_producto_index`(`id_producto`);
ALTER TABLE `opiniones` ADD INDEX `opiniones_id_usuario_index`(`id_usuario`);
ALTER TABLE `opiniones` ADD CONSTRAINT `opiniones_id_producto_foreign` FOREIGN KEY(`id_producto`) REFERENCES `productos`(`id_producto`);
ALTER TABLE `opiniones` ADD CONSTRAINT `opiniones_id_usuario_foreign` FOREIGN KEY(`id_usuario`) REFERENCES `usuarios`(`id_usuario`);

CREATE TABLE `opiniones_mod` (
    `id_opinion_mod` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_opinion` INT NOT NULL,
    `descripcion_anterior` TEXT NULL,
    `calificacion_anterior` INT NULL,
    `fecha_modificacion` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
    `motivo_edicion` TEXT NULL
);
ALTER TABLE `opiniones_mod` ADD INDEX `opiniones_mod_id_opinion_index`(`id_opinion`);
ALTER TABLE `opiniones_mod` ADD CONSTRAINT `opiniones_mod_id_opinion_foreign` FOREIGN KEY(`id_opinion`) REFERENCES `opiniones`(`id_opinion`);

CREATE TABLE `detalles_pedido` (
    `id_detalle` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_pedido` INT NOT NULL,
    `id_carrito` INT NOT NULL,
    `cantidad` INT NOT NULL,
    `precio` DECIMAL(10, 2) NOT NULL,
    `subtotal` DECIMAL(10, 2) NOT NULL
);
ALTER TABLE `detalles_pedido` ADD UNIQUE `detalles_pedido_id_carrito_unique`(`id_carrito`);
ALTER TABLE `detalles_pedido` ADD CONSTRAINT `detalles_pedido_id_carrito_foreign` FOREIGN KEY(`id_carrito`) REFERENCES `carritos`(`id_carrito`);

CREATE TABLE `pedidos` (
    `id_pedido` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_usuario` INT NOT NULL,
    `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
    `estado` ENUM('') NULL DEFAULT 'PENDIENTE',
    `id_detalle` BIGINT NOT NULL
);
ALTER TABLE `pedidos` ADD INDEX `pedidos_id_usuario_index`(`id_usuario`);
ALTER TABLE `pedidos` ADD CONSTRAINT `pedidos_id_usuario_foreign` FOREIGN KEY(`id_usuario`) REFERENCES `usuarios`(`id_usuario`);
ALTER TABLE `pedidos` ADD CONSTRAINT `pedidos_id_detalle_foreign` FOREIGN KEY(`id_detalle`) REFERENCES `detalles_pedido`(`id_detalle`);

CREATE TABLE `detalles_transaccion` (
    `id_detalle_transaccion` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_transaccion` INT NOT NULL,
    `codigo_rastreo` VARCHAR(100) NULL,
    `fecha_procesamiento` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
    `metodo_pago` VARCHAR(255) NULL
);

CREATE TABLE `transacciones` (
    `id_transaccion` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_pedido` INT NOT NULL,
    `estado` ENUM('') NULL DEFAULT 'PENDIENTE',
    `id_detalles_transaccion` BIGINT NOT NULL
);
ALTER TABLE `transacciones` ADD INDEX `transacciones_id_pedido_index`(`id_pedido`);
ALTER TABLE `transacciones` ADD UNIQUE `transacciones_id_detalles_transaccion_unique`(`id_detalles_transaccion`);
ALTER TABLE `transacciones` ADD CONSTRAINT `transacciones_id_pedido_foreign` FOREIGN KEY(`id_pedido`) REFERENCES `pedidos`(`id_pedido`);
ALTER TABLE `transacciones` ADD CONSTRAINT `transacciones_id_detalles_transaccion_foreign` FOREIGN KEY(`id_detalles_transaccion`) REFERENCES `detalles_transaccion`(`id_detalle_transaccion`);