-- Guía SQL 51–60: mismos tipos de operaciones sobre datos ficticios.
-- La transacción se revierte al terminar para poder repetir la práctica.
START TRANSACTION;
-- 51. Alta con todos los campos.
INSERT INTO clientes VALUES (200,'Luis','Ejemplo','1954-06-01','30000001','Argentina','Calle Ejemplo 400','Belgrano','000-003','luis@example.test');
-- 52. Alta múltiple en una sola sentencia.
INSERT INTO clientes VALUES
(201,'Eva','Ensayo','1991-01-10','30000002','Argentina','Calle Ejemplo 401','Flores','000-004','eva@example.test'),
(202,'Leo','Muestra','1992-02-20','30000003','Chile','Calle Ejemplo 402','Palermo','000-005','leo@example.test'),
(203,'Sol','Modelo','1993-03-30','30000004','Uruguay','Calle Ejemplo 403','Almagro','000-006','sol@example.test');
-- 53. Alta indicando explícitamente las columnas.
INSERT INTO clientes (id,nombre,apellido,nacimiento,dni,nacionalidad,domicilio,barrio,telefono,email) VALUES (204,'Maria Sol','Ejercicio','1995-07-01','30000005','Argentina','Calle Ejemplo 404','Recoleta','000-007','mariasol@example.test');
-- 54. Corregir apellido de un cliente identificado por clave primaria.
UPDATE clientes SET apellido='Chaves' WHERE id=85;
-- 55. Completar a ocho caracteres los documentos de siete dígitos.
UPDATE clientes SET dni=LPAD(dni,8,'0') WHERE CHAR_LENGTH(dni)=7;
-- 56. Corregir el nombre exacto, sin cambiar compuestos ni coincidencias parciales.
UPDATE clientes SET nombre='Nicolás' WHERE nombre='Nicolas';
-- 57. Apellidos extranjeros en mayúsculas.
UPDATE clientes SET apellido=UPPER(apellido) WHERE nacionalidad<>'Argentina';
-- 58. Baja por clave primaria.
DELETE FROM clientes WHERE id=9804;
-- 59. Baja por servidor de correo, sin confundirlo con una parte del usuario.
DELETE FROM clientes WHERE SUBSTRING_INDEX(email,'@',-1) IN ('z0h0','z0h0.test');
-- 60. Baja por barrio.
DELETE FROM clientes WHERE barrio='Flores';
SELECT * FROM clientes ORDER BY id;
ROLLBACK;
