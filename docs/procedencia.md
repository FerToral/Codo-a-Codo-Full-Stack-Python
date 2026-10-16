# Procedencia y alcance

Los quince scripts proceden de la carpeta personal [Ejercicios.Python](https://drive.google.com/drive/folders/1-IqZ5lJI79P3rDOXjRQk8CtHG_o902OP) de Google Drive. Fernando Toralez los identificó como prácticas realizadas durante su formación Codo a Codo Full Stack. El nombre de un archivo o su fecha, por sí solos, no identifican una comisión.

La colección tiene marcas históricas de marzo de 2020. La carpeta compartida del curso contiene un cronograma agosto–diciembre de 2020. La pertenencia a Codo a Codo está confirmada por el autor; la relación con esa edición concreta y con cada consigna sigue abierta. Los ejercicios no corresponden a la cursada de Introducción a la Programación UBA del segundo cuatrimestre de 2025.

## Correspondencia de archivos

Las rutas originales son las entradas del ZIP exportado de `Ejercicios.Python`. Los nombres actuales describen el contenido. El archivo originalmente denominado «copia» contiene una calculadora distinta del ejercicio de máximo, por lo que se conserva como una práctica independiente.

| Archivo original | Ubicación actual | Tratamiento |
| --- | --- | --- |
| `PrimerasFunciones.py` | `Python/01-funciones/suma.py` | Código conservado |
| `PruebaDeListas.py` | `Python/02-colecciones/listas.py` | Código conservado |
| `PracticasTuplas.py` | `Python/02-colecciones/tuplas.py` | Datos de ejemplo sintéticos |
| `PruebaDiccionarios.py` | `Python/02-colecciones/diccionarios.py` | Código conservado |
| `EjericiciosCondicionales-video11-2.py` | `Python/02-colecciones/datos_personales.py` | Código conservado; datos solicitados al ejecutar |
| `PracticasCondicionales.py` | `Python/03-condicionales/evaluacion.py` | Código conservado |
| `PracticasIF-ELSE.py` | `Python/03-condicionales/edad_y_notas.py` | Retirada una salida informal ajena al ejercicio |
| `PracticaCondicional2.py` | `Python/03-condicionales/asignaturas.py` | Código conservado |
| `EjericiciosCondicionales-video11-1.py` | `Python/03-condicionales/maximo.py` | Valida ambas notas, función importable y manejo de entrada |
| `EjericiciosCondicionales-video11-1 - copia.py` | `Python/03-condicionales/calculadora.py` | División por cero, operación desconocida y entrada inválida |
| `EjericiciosCondicionales-video11-3.py` | `Python/03-condicionales/media_aritmetica.py` | Una captura de tres notas y función sin contador global |
| `EjericiciosCondicionales-video17.py` | `Python/04-bucles-y-generadores/suma_positivos.py` | Código conservado |
| `PracticaBucle2.py` | `Python/04-bucles-y-generadores/buscar_arroba.py` | Código conservado; ejemplo de búsqueda, no validador completo de correo |
| `PracticasGeneradores.py` | `Python/04-bucles-y-generadores/generadores.py` | Código conservado |
| `video21/prueba_excepciones.py` | `Python/05-excepciones/raiz_cuadrada.py` | Conversión dentro del bloque de manejo de errores |

Los originales completos, con los comentarios de los ejemplos sustituidos en cuatro prácticas, siguen en el respaldo de Drive. No se eliminaron ni sobrescribieron.

## Matriz de evidencia

| Conjunto | Origen | Qué está confirmado | Qué falta |
| --- | --- | --- | --- |
| Quince scripts personales | Ejercicios.Python de Drive | Prácticas personales y pertenencia a Codo a Codo identificadas por Fernando Toralez | Comisión, cronograma y consigna exactos |
| Material Full Stack 2020 | Carpeta compartida CaC 2020 | Estructura de temas y cronograma agosto–diciembre | Correspondencia exacta con las prácticas de marzo |
| Proyecto2019 / TiendaEnLinea | Material de clase/Django/ProyectosDjango | Proyectos de referencia con `manage.py`; Tienda incluye modelos y migración | Una entrega propia o derivada acreditada |
| SQL y guías | Material de clase/Base de datos | Ejemplos y guías MySQL | Carpeta del proyecto PostgreSQL recordado por el autor |
| TP HTML/CSS y Vue | Trabajos prácticos | Consignas y carpetas de ejemplos | Versiones personales y resultado de cada entrega |
| Coderhouse, ITBA/Colab, UBA, DevOps y Testing | Otras formaciones | Cursos con contextos distintos | Se estudian en sus propios conjuntos, sin incorporarlos aquí |

## Validación y límites

Las pruebas verifican los errores concretos corregidos y ejecutan los quince archivos con entradas de ejemplo. No equivalen a una corrección oficial de los enunciados. Los scripts conservados pueden esperar entradas de un tipo concreto, como en su uso original de clase. En particular, `buscar_arroba.py` solo comprueba si aparece `@`, y `edad_y_notas.py` conserva las reglas históricas del ejemplo.
