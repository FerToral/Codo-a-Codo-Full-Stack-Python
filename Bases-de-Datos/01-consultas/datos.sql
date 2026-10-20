-- Datos ficticios y reducidos para practicar sin importar padrones ni bases personales.
-- Ejecutar sobre una base NUEVA dedicada al ejercicio. No contiene DROP DATABASE.
CREATE TABLE country (
 Code CHAR(3) PRIMARY KEY, Name VARCHAR(52) NOT NULL, Continent VARCHAR(20),
 Region VARCHAR(40), SurfaceArea DECIMAL(12,2), IndepYear SMALLINT,
 Population INT, LifeExpectancy DECIMAL(4,1), GNP DECIMAL(12,2), GNPOld DECIMAL(12,2),
 LocalName VARCHAR(52), GovernmentForm VARCHAR(45), Capital INT NULL
);
CREATE TABLE city (ID INT PRIMARY KEY, Name VARCHAR(40), CountryCode CHAR(3) NOT NULL,
 District VARCHAR(40), Population INT, FOREIGN KEY (CountryCode) REFERENCES country(Code));
CREATE TABLE countrylanguage (CountryCode CHAR(3), Language VARCHAR(40),
 IsOfficial CHAR(1), Percentage DECIMAL(4,1), PRIMARY KEY(CountryCode,Language),
 FOREIGN KEY(CountryCode) REFERENCES country(Code));
INSERT INTO country VALUES
('ARG','Argentina','South America','South America',2780400,1816,37000000,75.1,340000,330000,'Argentina','Federal Republic',1),
('URY','Uruguay','South America','South America',176215,1828,3300000,75.2,22000,21000,'Uruguay','Republic',3),
('ESP','Spain','Europe','Southern Europe',505992,1492,40000000,79.1,550000,540000,'España','Constitutional Monarchy',4),
('GBR','United Kingdom','Europe','British Islands',242900,1066,60000000,78.5,1400000,1350000,'United Kingdom','Constitutional Monarchy',5),
('JAM','Jamaica','North America','Caribbean',10990,1962,2600000,75.2,6500,6200,'Jamaica','Constitutional Monarchy',6),
('CUB','Cuba','North America','Caribbean',110861,1902,11000000,76.2,17000,16000,'Cuba','Socialistic Republic',7),
('ZAF','South Africa','Africa','Southern Africa',1221037,1910,40000000,52.1,126000,120000,'South Africa','Republic',8),
('JPN','Japan','Asia','Eastern Asia',377829,-660,126000000,81.0,4500000,4400000,'Nihon','Constitutional Monarchy',9),
('VAT','Holy See','Europe','Southern Europe',0.44,1929,1000,83.0,0,NULL,'Santa Sede','Independent Church State',10),
('ATA','Antarctica','Antarctica','Antarctica',13120000,NULL,0,NULL,0,NULL,'Antarctica','Co-administrated',NULL);
INSERT INTO city VALUES
(1,'Buenos Aires','ARG','Buenos Aires',2900000),(2,'Córdoba','ARG','Córdoba',1250000),
(3,'Montevideo','URY','Montevideo',1300000),(4,'Madrid','ESP','Madrid',2800000),
(5,'London','GBR','England',7200000),(6,'Kingston','JAM','Saint Andrew',700000),
(7,'La Habana','CUB','La Habana',2200000),(8,'Pretoria','ZAF','Pretoria',600000),
(9,'Tokyo','JPN','Tokyo',8000000),(10,'Vatican City','VAT','Vatican City',1000),
(11,'Villa del Sol','ARG','Buenos Aires',128000),(12,'Port-Example','JAM','Saint Andrew',8000),
(13,'Pequeña Villa','URY','Interior',3000),(14,'Liverpool','GBR','England',500000);
INSERT INTO countrylanguage VALUES
('ARG','Spanish','T',96.0),('ARG','Italian','F',2.0),('ARG','Guarani','F',1.0),
('URY','Spanish','T',98.0),('URY','Portuguese','F',1.0),('ESP','Spanish','T',74.0),
('ESP','Catalan','F',16.0),('ESP','Basque','F',2.0),('GBR','English','T',98.0),
('JAM','English','T',99.0),('CUB','Spanish','T',100.0),('ZAF','English','T',8.0),
('ZAF','Zulu','T',24.0),('ZAF','Afrikaans','T',14.0),('JPN','Japanese','T',99.0),
('VAT','Italian','T',100.0);
