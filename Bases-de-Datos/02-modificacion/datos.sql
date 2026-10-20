CREATE TABLE clientes (
 id INT PRIMARY KEY, nombre VARCHAR(60), apellido VARCHAR(60), nacimiento DATE,
 dni VARCHAR(8), nacionalidad VARCHAR(40), domicilio VARCHAR(100), barrio VARCHAR(50),
 telefono VARCHAR(30), email VARCHAR(100)
);
INSERT INTO clientes VALUES
(85,'Nicolas','Chavez','1990-04-05','1234567','Argentina','Calle Ejemplo 100','Caballito','000-000','nicolas@example.test'),
(9804,'Ana','Demo','1985-02-01','2345678','Uruguay','Calle Ejemplo 200','Flores','000-001','ana@z0h0.test'),
(100,'Irene','Prueba','1994-09-10','12345678','Chile','Calle Ejemplo 300','Almagro','000-002','irene@example.test');
