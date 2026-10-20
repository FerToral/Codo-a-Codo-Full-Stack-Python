-- Guía práctica de SQL, ejercicios 1–50. Dialecto MySQL/MariaDB.
-- Cada consulta se ejecuta de forma independiente sobre las tablas country, city y countrylanguage.
-- 01. Código, nombre, continente y población.
SELECT Code, Name, Continent, Population FROM country;
-- 02. Idiomas sin repetición.
SELECT DISTINCT Language FROM countrylanguage;
-- 03. Alias en español.
SELECT Name AS Nombre, Population AS Poblacion FROM city;
-- 04. Diferencia entre PNB actual y anterior; NULL se mantiene como dato desconocido.
SELECT Name, GNP, GNPOld, GNP-GNPOld AS Diferencia FROM country;
-- 05. Densidad; dividir por una superficie cero produce NULL.
SELECT Name, Population, SurfaceArea, Population/NULLIF(SurfaceArea,0) AS Densidad FROM country;
-- 06. Población ascendente.
SELECT * FROM country ORDER BY Population ASC, Code;
-- 07. Idiomas en orden alfabético, incluidas repeticiones.
SELECT Language FROM countrylanguage ORDER BY Language;
-- 08. Las veinte ciudades menos pobladas.
SELECT * FROM city ORDER BY Population ASC, ID LIMIT 20;
-- 09. Independencia: primero los países más antiguos; al final, los años desconocidos.
SELECT Code, Name, IndepYear FROM country ORDER BY IndepYear IS NULL, IndepYear ASC, Code;
-- 10. Cien mayores esperanzas de vida; empate por menor superficie.
SELECT * FROM country ORDER BY LifeExpectancy DESC, SurfaceArea ASC, Code LIMIT 100;
-- 11. Países sin población.
SELECT * FROM country WHERE Population=0;
-- 12. Esperanza de vida mayor que 75.
SELECT * FROM country WHERE LifeExpectancy>75 ORDER BY LifeExpectancy, Code;
-- 13. Monarquías constitucionales independizadas a partir de 1850.
SELECT * FROM country WHERE IndepYear>=1850 AND GovernmentForm='Constitutional Monarchy';
-- 14. Diez mayores PNB europeos.
SELECT * FROM country WHERE Continent='Europe' ORDER BY GNP DESC, Code LIMIT 10;
-- 15. Nombre internacional igual al local.
SELECT * FROM country WHERE Name=LocalName;
-- 16. Independencia desde 1950 inclusive.
SELECT * FROM country WHERE IndepYear>=1950;
-- 17. Países de Europa, Asia o Sudamérica.
SELECT * FROM country WHERE Continent IN ('Europe','Asia','South America');
-- 18. Países fuera de África.
SELECT * FROM country WHERE Continent<>'Africa';
-- 19. Ciudades argentinas fuera del distrito Buenos Aires.
SELECT * FROM city WHERE CountryCode='ARG' AND District<>'Buenos Aires';
-- 20. Entre 125000 y 130000 habitantes, extremos incluidos.
SELECT * FROM city WHERE Population BETWEEN 125000 AND 130000;
-- 21. Independencia desconocida.
SELECT * FROM country WHERE IndepYear IS NULL;
-- 22. Sin PNB anterior ni esperanza de vida.
SELECT * FROM country WHERE GNPOld IS NULL AND LifeExpectancy IS NULL;
-- 23. Nombres que empiezan y terminan en A, sin distinguir mayúsculas.
SELECT * FROM country WHERE LOWER(Name) LIKE 'a%a';
-- 24. Nombre con al menos un espacio.
SELECT * FROM country WHERE Name LIKE '% %';
-- 25. Guiones en ciudad o distrito.
SELECT * FROM city WHERE Name LIKE '%-%' OR District LIKE '%-%';
-- 26. Todos los países sudamericanos, incluso si no se conoce su capital.
SELECT p.Name AS Pais, c.Name AS Capital FROM country p LEFT JOIN city c ON c.ID=p.Capital WHERE p.Continent='South America';
-- 27. Ciudades de países con esperanza de vida mayor que 80.
SELECT c.CountryCode, c.Name, c.Population FROM city c JOIN country p ON p.Code=c.CountryCode WHERE p.LifeExpectancy>80;
-- 28. Repúblicas federales con su capital.
SELECT p.Name AS Pais, c.Name AS Capital FROM country p LEFT JOIN city c ON c.ID=p.Capital WHERE p.GovernmentForm='Federal Republic';
-- 29. Idiomas oficiales de países entre uno y tres millones de habitantes.
SELECT p.Name, l.Language FROM country p JOIN countrylanguage l ON l.CountryCode=p.Code WHERE p.Population BETWEEN 1000000 AND 3000000 AND l.IsOfficial='T';
-- 30. Países donde se habla español, sea o no oficial.
SELECT p.Code, p.LocalName, p.Region FROM country p WHERE EXISTS (SELECT 1 FROM countrylanguage l WHERE l.CountryCode=p.Code AND l.Language='Spanish');
-- 31. Capital con más de la mitad de la población nacional.
SELECT p.Name AS Pais, c.Name AS Capital FROM country p JOIN city c ON c.ID=p.Capital WHERE c.Population>p.Population/2;
-- 32. Países africanos cuya capital coincide con el distrito de la ciudad.
SELECT p.Name, p.SurfaceArea FROM country p JOIN city c ON c.ID=p.Capital WHERE p.Continent='Africa' AND c.Name=c.District;
-- 33. Veinte independencias más antiguas conocidas.
SELECT p.Name AS Pais, c.Name AS Capital, p.IndepYear FROM country p LEFT JOIN city c ON c.ID=p.Capital WHERE p.IndepYear IS NOT NULL ORDER BY p.IndepYear, p.Code LIMIT 20;
-- 34. Excluir países con cualquiera de los seis idiomas oficiales indicados.
SELECT c.Name AS Ciudad, p.Name AS Pais, l.Language FROM city c JOIN country p ON p.Code=c.CountryCode JOIN countrylanguage l ON l.CountryCode=p.Code AND l.IsOfficial='T' WHERE NOT EXISTS (SELECT 1 FROM countrylanguage x WHERE x.CountryCode=p.Code AND x.IsOfficial='T' AND x.Language IN ('Spanish','English','Portuguese','Italian','French','German'));
-- 35. Diez ciudades europeas más pobladas de países donde se habla inglés.
SELECT c.Name, c.Population, p.Name AS Pais FROM city c JOIN country p ON p.Code=c.CountryCode WHERE p.Continent='Europe' AND EXISTS (SELECT 1 FROM countrylanguage l WHERE l.CountryCode=p.Code AND l.Language='English') ORDER BY c.Population DESC, c.ID LIMIT 10;
-- 36. Estadísticas globales.
SELECT SUM(Population), MAX(Population), MIN(Population), AVG(Population), COUNT(*) FROM country;
-- 37. Estadísticas por continente.
SELECT Continent, SUM(Population), MAX(Population), MIN(Population), AVG(Population), COUNT(*) FROM country GROUP BY Continent;
-- 38. Cantidad de países por continente.
SELECT Continent, COUNT(*) AS Cantidad FROM country GROUP BY Continent;
-- 39. Población urbana por código de país.
SELECT CountryCode, SUM(Population) AS Poblacion FROM city GROUP BY CountryCode;
-- 40. Mínimo porcentaje por idioma.
SELECT Language, MIN(Percentage) AS Minimo FROM countrylanguage GROUP BY Language;
-- 41. Población media por forma de gobierno europea.
SELECT GovernmentForm, AVG(Population) AS Promedio FROM country WHERE Continent='Europe' GROUP BY GovernmentForm;
-- 42. Diez regiones con mayor esperanza media de vida.
SELECT Region, AVG(LifeExpectancy) AS Promedio FROM country GROUP BY Region ORDER BY Promedio DESC, Region LIMIT 10;
-- 43. Distritos con más ciudades de más de 500000 habitantes; el país evita homónimos.
SELECT CountryCode, District, COUNT(*) AS Ciudades FROM city WHERE Population>500000 GROUP BY CountryCode, District ORDER BY Ciudades DESC, CountryCode, District LIMIT 10;
-- 44. Ciudades por país caribeño, incluidos países sin ciudades registradas.
SELECT p.Code, p.Name, COUNT(c.ID) AS Ciudades FROM country p LEFT JOIN city c ON c.CountryCode=p.Code WHERE p.Region='Caribbean' GROUP BY p.Code,p.Name;
-- 45. Países por idioma oficial.
SELECT Language, COUNT(*) AS Paises FROM countrylanguage WHERE IsOfficial='T' GROUP BY Language;
-- 46. Años de independencia compartidos por al menos dos países.
SELECT IndepYear, COUNT(*) AS Paises FROM country WHERE IndepYear IS NOT NULL GROUP BY IndepYear HAVING COUNT(*)>1;
-- 47. Países con tres a cinco idiomas registrados.
SELECT p.Code,p.Name,COUNT(l.Language) AS Idiomas FROM country p JOIN countrylanguage l ON l.CountryCode=p.Code GROUP BY p.Code,p.Name HAVING COUNT(l.Language) BETWEEN 3 AND 5;
-- 48. Distritos con población urbana total no mayor que 10000.
SELECT CountryCode,District,SUM(Population) AS Poblacion FROM city GROUP BY CountryCode,District HAVING SUM(Population)<=10000;
-- 49. Regiones cuya densidad media supera la mitad de la mayor densidad nacional.
SELECT Region,AVG(Population/NULLIF(SurfaceArea,0)) AS Densidad FROM country GROUP BY Region HAVING AVG(Population/NULLIF(SurfaceArea,0))>(SELECT MAX(Population/NULLIF(SurfaceArea,0))/2 FROM country);
-- 50. Idiomas oficiales con porcentaje promedio de un solo dígito entero (hasta 9).
SELECT Language,AVG(Percentage) AS Promedio FROM countrylanguage WHERE IsOfficial='T' GROUP BY Language HAVING AVG(Percentage)<=9;
