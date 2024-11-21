-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: eleganza_ecommerce
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carrito_items`
--

DROP TABLE IF EXISTS `carrito_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito_items` (
  `id_carrito_item` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` int NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_carrito_item`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `carrito_items_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `carrito_items_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito_items`
--

LOCK TABLES `carrito_items` WRITE;
/*!40000 ALTER TABLE `carrito_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `carrito_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carritos`
--

DROP TABLE IF EXISTS `carritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carritos` (
  `id_carrito` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_producto` int NOT NULL,
  PRIMARY KEY (`id_carrito`),
  UNIQUE KEY `carritos_id_usuario_unique` (`id_usuario`),
  KEY `carritos_id_producto_index` (`id_producto`),
  CONSTRAINT `carritos_id_producto_foreign` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `carritos_id_usuario_foreign` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carritos`
--

LOCK TABLES `carritos` WRITE;
/*!40000 ALTER TABLE `carritos` DISABLE KEYS */;
/*!40000 ALTER TABLE `carritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cupones`
--

DROP TABLE IF EXISTS `cupones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cupones` (
  `id_cupon` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(20) NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `solo_vip` tinyint(1) DEFAULT '1',
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_cupon`),
  UNIQUE KEY `cupones_codigo_unique` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cupones`
--

LOCK TABLES `cupones` WRITE;
/*!40000 ALTER TABLE `cupones` DISABLE KEYS */;
/*!40000 ALTER TABLE `cupones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalles_pedido`
--

DROP TABLE IF EXISTS `detalles_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_pedido` (
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `id_pedido` int NOT NULL,
  `id_carrito` int NOT NULL,
  `cantidad` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_detalle`),
  UNIQUE KEY `detalles_pedido_id_carrito_unique` (`id_carrito`),
  CONSTRAINT `detalles_pedido_id_carrito_foreign` FOREIGN KEY (`id_carrito`) REFERENCES `carritos` (`id_carrito`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_pedido`
--

LOCK TABLES `detalles_pedido` WRITE;
/*!40000 ALTER TABLE `detalles_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalles_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalles_transaccion`
--

DROP TABLE IF EXISTS `detalles_transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_transaccion` (
  `id_detalle_transaccion` int NOT NULL AUTO_INCREMENT,
  `id_transaccion` int NOT NULL,
  `codigo_rastreo` varchar(100) DEFAULT NULL,
  `fecha_procesamiento` datetime DEFAULT CURRENT_TIMESTAMP,
  `metodo_pago` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_detalle_transaccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_transaccion`
--

LOCK TABLES `detalles_transaccion` WRITE;
/*!40000 ALTER TABLE `detalles_transaccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalles_transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opiniones`
--

DROP TABLE IF EXISTS `opiniones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opiniones` (
  `id_opinion` int NOT NULL AUTO_INCREMENT,
  `id_producto` int NOT NULL,
  `id_usuario` int NOT NULL,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP,
  `descripcion` text,
  `calificacion` int DEFAULT NULL,
  `estado` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_opinion`),
  KEY `opiniones_id_producto_index` (`id_producto`),
  KEY `opiniones_id_usuario_index` (`id_usuario`),
  CONSTRAINT `opiniones_id_producto_foreign` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `opiniones_id_usuario_foreign` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opiniones`
--

LOCK TABLES `opiniones` WRITE;
/*!40000 ALTER TABLE `opiniones` DISABLE KEYS */;
/*!40000 ALTER TABLE `opiniones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opiniones_mod`
--

DROP TABLE IF EXISTS `opiniones_mod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opiniones_mod` (
  `id_opinion_mod` int NOT NULL AUTO_INCREMENT,
  `id_opinion` int NOT NULL,
  `descripcion_anterior` text,
  `calificacion_anterior` int DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `motivo_edicion` text,
  PRIMARY KEY (`id_opinion_mod`),
  KEY `opiniones_mod_id_opinion_index` (`id_opinion`),
  CONSTRAINT `opiniones_mod_id_opinion_foreign` FOREIGN KEY (`id_opinion`) REFERENCES `opiniones` (`id_opinion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opiniones_mod`
--

LOCK TABLES `opiniones_mod` WRITE;
/*!40000 ALTER TABLE `opiniones_mod` DISABLE KEYS */;
/*!40000 ALTER TABLE `opiniones_mod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `direccion_envio` varchar(255) NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP,
  `estado` enum('PENDIENTE','PROCESANDO','COMPLETADO','CANCELADO') DEFAULT 'PENDIENTE',
  `id_detalle` int DEFAULT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `pedidos_id_usuario_index` (`id_usuario`),
  KEY `pedidos_id_detalle_foreign` (`id_detalle`),
  CONSTRAINT `pedidos_id_detalle_foreign` FOREIGN KEY (`id_detalle`) REFERENCES `detalles_pedido` (`id_detalle`),
  CONSTRAINT `pedidos_id_usuario_foreign` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES (1,1,0.00,'a','tarjeta','2024-11-21 16:26:22','PENDIENTE',NULL),(2,1,0.00,'a','tarjeta','2024-11-21 16:30:05','PENDIENTE',NULL),(3,1,0.00,'a','tarjeta','2024-11-21 16:32:01','PENDIENTE',NULL),(4,1,0.00,'a','tarjeta','2024-11-21 16:33:18','PENDIENTE',NULL),(5,1,0.00,'a','tarjeta','2024-11-21 16:35:10','PENDIENTE',NULL),(6,1,0.00,'a','tarjeta','2024-11-21 16:36:58','PENDIENTE',NULL),(7,1,0.00,'a','tarjeta','2024-11-21 16:38:46','PENDIENTE',NULL),(8,1,0.00,'a','tarjeta','2024-11-21 16:44:00','PENDIENTE',NULL),(9,1,0.00,'a','tarjeta','2024-11-21 16:45:37','PENDIENTE',NULL),(10,1,0.00,'a','tarjeta','2024-11-21 16:47:52','PENDIENTE',NULL),(11,1,0.00,'a','tarjeta','2024-11-21 16:51:53','PENDIENTE',NULL),(12,1,0.00,'a','tarjeta','2024-11-21 16:56:27','PENDIENTE',NULL);
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planes_vip`
--

DROP TABLE IF EXISTS `planes_vip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `planes_vip` (
  `id_plan` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `duracion` int NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  `id_cupones` int NOT NULL,
  PRIMARY KEY (`id_plan`),
  KEY `planes_vip_id_cupones_index` (`id_cupones`),
  CONSTRAINT `planes_vip_id_cupones_foreign` FOREIGN KEY (`id_cupones`) REFERENCES `cupones` (`id_cupon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planes_vip`
--

LOCK TABLES `planes_vip` WRITE;
/*!40000 ALTER TABLE `planes_vip` DISABLE KEYS */;
/*!40000 ALTER TABLE `planes_vip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `id_proveedor` int NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `stock` int NOT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT '1',
  `descuento` decimal(5,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`id_producto`),
  KEY `productos_id_proveedor_foreign` (`id_proveedor`),
  CONSTRAINT `productos_id_proveedor_foreign` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (2,1,'Vestido elegante para cuaqluier ocación',300000.00,'Vestido Elegante',10,NULL,1,0.00);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `id_tipo_proveedor` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` text,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_proveedor`),
  KEY `proveedores_id_tipo_proveedor_foreign` (`id_tipo_proveedor`),
  CONSTRAINT `proveedores_id_tipo_proveedor_foreign` FOREIGN KEY (`id_tipo_proveedor`) REFERENCES `tipo_proveedor` (`id_tipo_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (1,1,'Eleganza Fashion','Calle Principal 123','3001234567','eleganza@fashion.com',1);
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_de_rol` varchar(50) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suscripciones_vip`
--

DROP TABLE IF EXISTS `suscripciones_vip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_vip` (
  `id_suscripcion` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_plan` int NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_suscripcion`),
  KEY `suscripciones_vip_id_usuario_index` (`id_usuario`),
  KEY `suscripciones_vip_id_plan_index` (`id_plan`),
  CONSTRAINT `suscripciones_vip_id_plan_foreign` FOREIGN KEY (`id_plan`) REFERENCES `planes_vip` (`id_plan`),
  CONSTRAINT `suscripciones_vip_id_usuario_foreign` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_vip`
--

LOCK TABLES `suscripciones_vip` WRITE;
/*!40000 ALTER TABLE `suscripciones_vip` DISABLE KEYS */;
/*!40000 ALTER TABLE `suscripciones_vip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_proveedor`
--

DROP TABLE IF EXISTS `tipo_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_proveedor` (
  `id_tipo_proveedor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_tipo_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_proveedor`
--

LOCK TABLES `tipo_proveedor` WRITE;
/*!40000 ALTER TABLE `tipo_proveedor` DISABLE KEYS */;
INSERT INTO `tipo_proveedor` VALUES (1,'Mayorista','Proveedor de grandes cantidades');
/*!40000 ALTER TABLE `tipo_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transacciones`
--

DROP TABLE IF EXISTS `transacciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transacciones` (
  `id_transaccion` int NOT NULL AUTO_INCREMENT,
  `id_pedido` int NOT NULL,
  `estado` enum('PENDIENTE','PROCESANDO','COMPLETADO','FALLIDO') DEFAULT 'PENDIENTE',
  `id_detalles_transaccion` int NOT NULL,
  PRIMARY KEY (`id_transaccion`),
  UNIQUE KEY `transacciones_id_detalles_transaccion_unique` (`id_detalles_transaccion`),
  KEY `transacciones_id_pedido_index` (`id_pedido`),
  CONSTRAINT `transacciones_id_detalles_transaccion_foreign` FOREIGN KEY (`id_detalles_transaccion`) REFERENCES `detalles_transaccion` (`id_detalle_transaccion`),
  CONSTRAINT `transacciones_id_pedido_foreign` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transacciones`
--

LOCK TABLES `transacciones` WRITE;
/*!40000 ALTER TABLE `transacciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `transacciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `id_rol` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `es_vip` tinyint(1) DEFAULT '0',
  `estado` tinyint(1) DEFAULT '1',
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`),
  KEY `usuarios_id_rol_index` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,2,'juan','juanperez@gmail.com','scrypt:32768:8:1$9bXYfkHceHfFeHmq$3db256d97663add5349a53bada2f24adbe3abab1f88549db0007c0d4f8442108931b98ed62370da4bd2198e7ec388e75157935dbb6e01563dc0ddbaa5568a3a7',0,1,'2024-11-19 04:05:23'),(2,2,'jairo','jairoperez@gmail.com','scrypt:32768:8:1$vumLvFKrDylconuV$0e5abe459ddf85cfa5334d007a69afc3e2235ea0a3a7fd3a5c11513585ca963cfd2b274bace3aedfcce094549e349019649ae304bc1a2cc1bdf3f3c3e3b49fc6',0,1,'2024-11-19 04:12:42'),(3,2,'michael','michaelosppino@gmail.com','scrypt:32768:8:1$taBllm0aduqZclaJ$1464cbd45e0a948e5d0e7332ce7a1d80085c3fab1f6596653820094ce80537d02fc8be7e76a0c069d7c3a6757707e8d1808b3777f26c0ed875bb4c5aa1d2bafc',0,1,'2024-11-19 04:52:54'),(4,2,'daniela','daniela-villasb@gmail.com','scrypt:32768:8:1$NYRLw3Ztq0QQAH0c$f958dc9e95f2b7e245c56274af2f9771ca7f05eb222d4d63580dd2780972f1301a8668b7b7ad0316a0ea7d3f9ff58af145873cc3cb7b0b2247fc8d2271bb0bee',0,1,'2024-11-19 06:34:56'),(5,2,'prueba','prueba@gmail.com','scrypt:32768:8:1$vG1sKtkK9VZWXMf3$287c4a842d1620e19fb4b1436a5f46844ee71337311018f178a1157a64db9da27b4188d66446888823d59a0ba27f1ab97b1df87ceedfefd8b68b546db9290bcc',0,1,'2024-11-21 00:20:05');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-21 12:32:37
