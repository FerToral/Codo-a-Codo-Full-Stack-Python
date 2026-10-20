# Bases de datos

Prácticas de SQL con consultas, relaciones y modificación de registros. El dialecto es MySQL/MariaDB.

| Carpeta | Actividad |
| --- | --- |
| `01-consultas` | Ejercicios 1–50: filtros, ordenación, joins, subconsultas y agregaciones |
| `02-modificacion` | Ejercicios 51–60: altas, cambios y bajas dentro de una transacción |
| `03-empleados` | 35 ejercicios sobre empleados, departamentos y jefaturas |

La [guía original de Carlos E. Cimino](Guias/Guia-practica-SQL.pdf) está incluida completa, con su licencia CC BY-NC-ND 4.0. Las consultas se encuentran en archivos separados para poder trabajar con el enunciado y la solución a la vez.

## Preparar las prácticas

Crear tres bases **nuevas y vacías**, una por carpeta. Desde un cliente MySQL, conectado a la base correspondiente:

```sql
SOURCE 01-consultas/datos.sql;
SOURCE 01-consultas/consultas.sql;
```

Repetir con `02-modificacion` y `03-empleados`. También se pueden abrir los archivos en MySQL Workbench y ejecutar cada sentencia por separado. No utilizar una base personal o de producción. Los scripts de estructura no borran tablas existentes: si se repite la carga sobre una base ya inicializada, se informa el conflicto.

Los datos incluidos son ficticios y reducidos. El primer módulo conserva las tablas `country`, `city` y `countrylanguage` de la práctica World, pero no sus recuentos históricos; permite resolver los ejercicios sin descargar otra base. Los ejemplos de clientes usan correos `.test` y no reproducen el padrón de la guía. Para estudiar el esquema completo World también se puede importar el dataset oficial de MySQL en otra base vacía.

`operaciones.sql` termina con `ROLLBACK`, por lo que sus modificaciones no quedan guardadas. Para estudiar cada cambio, ejecutar las sentencias una a una y consultar la tabla antes del rollback.

## Modelo de empleados

Cada empleado pertenece a un departamento y puede tener un jefe. Cada departamento puede tener un director. Las tablas se cargan antes de agregar las claves de jefatura y dirección, para resolver las referencias circulares sin desactivar la integridad referencial. Los importes se guardan como `DECIMAL`, no como números de coma flotante.

La numeración y las decisiones sobre consultas ambiguas se indican en comentarios SQL. El ejercicio 10 de empleados tiene dos consultas; el 35 conserva todos los departamentos empatados en la mayor nómina.

Ver [consignas de empleados](03-empleados/CONSIGNAS.md) y [créditos](../CREDITOS.md).
