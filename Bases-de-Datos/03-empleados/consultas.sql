-- 01–09. Selección, proyección y ordenación.
SELECT * FROM empleados;
SELECT * FROM departamentos;
SELECT * FROM empleados WHERE cargoE='Secretaria';
SELECT nomEmp,salEmp FROM empleados;
SELECT * FROM empleados WHERE cargoE='Vendedor' ORDER BY nomEmp;
SELECT nombreDpto FROM departamentos;
SELECT nomEmp,cargoE FROM empleados ORDER BY salEmp;
SELECT salEmp,comisionE FROM empleados WHERE codDepto='2000' ORDER BY comisionE;
SELECT comisionE FROM empleados;
-- 10a. Nómina de producción con bonificación fija de 500000.
SELECT SUM(salEmp+500000) AS Nomina FROM empleados WHERE codDepto='3000';
-- 10b. Detalle individual.
SELECT nomEmp,salEmp,salEmp+500000 AS ConBonificacion FROM empleados WHERE codDepto='3000' ORDER BY nomEmp;
-- 11. Comisión mayor que el sueldo.
SELECT * FROM empleados WHERE comisionE>salEmp;
-- 12. Comisión no mayor al 30% del sueldo.
SELECT * FROM empleados WHERE comisionE<=salEmp*0.3;
-- 13. Concatenación de campos y etiquetas.
SELECT CONCAT('Nombre: ',nomEmp,' - Cargo: ',cargoE) AS Empleado FROM empleados;
-- 14. Documento numéricamente mayor que 19709802, aunque se almacena como texto.
SELECT * FROM empleados WHERE CAST(REPLACE(nDIEmp,'.','') AS UNSIGNED)>19709802;
-- 15. Inicial entre J y Z.
SELECT * FROM empleados WHERE UPPER(LEFT(nomEmp,1)) BETWEEN 'J' AND 'Z' ORDER BY nomEmp;
-- 16. Comisión mayor a un millón; ordenar numéricamente por documento.
SELECT nDIEmp,nomEmp,salEmp,comisionE,salEmp+comisionE AS Total FROM empleados WHERE comisionE>1000000 ORDER BY CAST(REPLACE(nDIEmp,'.','') AS UNSIGNED);
-- 17. Empleados con comisión.
SELECT nDIEmp,nomEmp,salEmp,comisionE,salEmp+comisionE AS Total FROM empleados WHERE comisionE>0 ORDER BY CAST(REPLACE(nDIEmp,'.','') AS UNSIGNED);
-- 18. Nombre sin la secuencia MA.
SELECT * FROM empleados WHERE UPPER(nomEmp) NOT LIKE '%MA%';
-- 19. Departamentos excluidos por nombre.
SELECT * FROM departamentos WHERE UPPER(nombreDpto) NOT IN ('VENTAS','INVESTIGACION','MANTENIMIENTO');
-- 20. Secretaría o ventas, fuera de producción y sueldo mayor a un millón.
SELECT e.* FROM empleados e JOIN departamentos d ON d.codDepto=e.codDepto WHERE e.cargoE IN ('Secretaria','Vendedor') AND d.nombreDpto<>'PRODUCCION' AND e.salEmp>1000000 ORDER BY e.fecIncorporacion;
-- 21. Nombre de once caracteres.
SELECT * FROM empleados WHERE CHAR_LENGTH(nomEmp)=11;
-- 22. Nombre de al menos once caracteres.
SELECT * FROM empleados WHERE CHAR_LENGTH(nomEmp)>=11;
-- 23. Nombre con M, en ventas, y sueldo alto o alguna comisión.
SELECT e.* FROM empleados e JOIN departamentos d ON d.codDepto=e.codDepto WHERE UPPER(e.nomEmp) LIKE 'M%' AND d.nombreDpto='VENTAS' AND (e.salEmp>800000 OR e.comisionE>0);
-- 24. Sueldo entre la mitad y el total de su propia comisión.
SELECT * FROM empleados WHERE salEmp BETWEEN comisionE/2 AND comisionE;
-- 25. Mayor sueldo.
SELECT MAX(salEmp) AS Maximo FROM empleados;
-- 26. Comisiones positivas y cantidad de empleados que las cobran.
SELECT comisionE,COUNT(*) AS Empleados FROM empleados WHERE comisionE>0 GROUP BY comisionE;
-- 27. Último nombre en orden alfabético, incluidos empates.
SELECT nomEmp FROM empleados WHERE nomEmp=(SELECT MAX(nomEmp) FROM empleados);
-- 28. Mayor, menor y diferencia.
SELECT MAX(salEmp),MIN(salEmp),MAX(salEmp)-MIN(salEmp) AS Diferencia FROM empleados;
-- 29. Cantidades por departamento y sexo.
SELECT codDepto,sexEmp,COUNT(*) AS Cantidad FROM empleados GROUP BY codDepto,sexEmp;
-- 30. Sueldo medio por departamento.
SELECT codDepto,AVG(salEmp) AS Promedio FROM empleados GROUP BY codDepto;
-- 31. Sueldo igual o superior a la media general.
SELECT * FROM empleados WHERE salEmp>=(SELECT AVG(salEmp) FROM empleados) ORDER BY codDepto,nDIEmp;
-- 32. Departamentos con más de tres empleados.
SELECT codDepto,COUNT(*) AS Cantidad FROM empleados GROUP BY codDepto HAVING COUNT(*)>3;
-- 33. Jefes con dos o más personas a cargo (la guía incluye explícitamente el dos).
SELECT j.nDIEmp,j.nomEmp,COUNT(e.nDIEmp) AS Personas FROM empleados j JOIN empleados e ON e.jefeID=j.nDIEmp GROUP BY j.nDIEmp,j.nomEmp HAVING COUNT(e.nDIEmp)>=2;
-- 34. Departamentos vacíos.
SELECT d.* FROM departamentos d LEFT JOIN empleados e ON e.codDepto=d.codDepto WHERE e.nDIEmp IS NULL;
-- 35. Mayor nómina departamental: conservar todos los empates.
SELECT codDepto,SUM(salEmp) AS Nomina FROM empleados GROUP BY codDepto HAVING SUM(salEmp)=(SELECT MAX(t.Nomina) FROM (SELECT SUM(salEmp) AS Nomina FROM empleados GROUP BY codDepto) t);
