-- Modelo relacional de empleados y departamentos; datos inventados.
-- Se crean ambas tablas antes de agregar las claves que forman un ciclo.
CREATE TABLE departamentos (codDepto VARCHAR(4) PRIMARY KEY, nombreDpto VARCHAR(20),ciudad VARCHAR(15),codDirector VARCHAR(12) NULL);
CREATE TABLE empleados (nDIEmp VARCHAR(12) PRIMARY KEY,nomEmp VARCHAR(30),sexEmp CHAR(1),fecNac DATE,fecIncorporacion DATE,salEmp DECIMAL(12,2),comisionE DECIMAL(12,2),cargoE VARCHAR(20),jefeID VARCHAR(12) NULL,codDepto VARCHAR(4),FOREIGN KEY (codDepto) REFERENCES departamentos(codDepto));
INSERT INTO departamentos VALUES ('1000','VENTAS','Buenos Aires',NULL),('2000','INVESTIGACION','Córdoba',NULL),('3000','PRODUCCION','Rosario',NULL),('4000','MANTENIMIENTO','Córdoba',NULL),('5000','ADMINISTRACION','La Plata',NULL);
INSERT INTO empleados VALUES
('10000001','Ana Modelo','F','1980-01-01','2010-01-01',2000000,0,'Director',NULL,'1000'),
('20000002','Juan Ensayo','M','1990-02-02','2015-02-01',1200000,500000,'Vendedor','10000001','1000'),
('20000003','Marta Prueba','F','1992-03-03','2017-03-01',900000,1000000,'Vendedor','10000001','1000'),
('20000004','Marcos Demo','M','1993-04-04','2018-04-01',800000,500000,'Vendedor','10000001','1000'),
('20000005','Julia Test','F','1991-05-05','2016-05-01',1500000,0,'Secretaria','10000001','2000'),
('10000006','Leo Ejemplo','M','1982-06-06','2011-06-01',2000000,100000,'Director',NULL,'3000'),
('20000007','Sol Ficticia','F','1995-07-07','2019-07-01',1100000,200000,'Operario','10000006','3000'),
('20000008','Nico Muestra','M','1994-08-08','2019-08-01',1300000,1500000,'Operario','10000006','3000');
UPDATE departamentos SET codDirector='10000001' WHERE codDepto IN ('1000','2000');
UPDATE departamentos SET codDirector='10000006' WHERE codDepto='3000';
ALTER TABLE empleados ADD CONSTRAINT fk_jefe FOREIGN KEY (jefeID) REFERENCES empleados(nDIEmp);
ALTER TABLE departamentos ADD CONSTRAINT fk_director FOREIGN KEY (codDirector) REFERENCES empleados(nDIEmp);
