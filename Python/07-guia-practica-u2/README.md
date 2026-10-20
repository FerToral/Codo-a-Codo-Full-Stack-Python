# Python · Guía práctica U2

Funciones, secuencias, cadenas y programas de consola. Soluciones nuevas
de mantenimiento de 2026, basadas en la guía de la carpeta compartida
de Codo a Codo Full Stack. No son archivos personales recuperados ni
se adscriben a una clase de marzo sólo por compartir temas.

## Consigna y recorrido

Fuente: **Python - Actividad Practica U2.pdf**, seis páginas,
en [Material de clase / Python](https://drive.google.com/drive/folders/1Fpgw944KMCjIpe4xY1KBQU8MWZISmCQ-).
El PDF se conserva en el respaldo privado con la teoría; aquí se enlaza
sin redistribuirlo ni reproducirlo íntegro.

| Ejercicios de la guía | Archivo | Contenido |
|---|---|---|
| 1–3 | funciones.py / consola.py | Producto, entrada/salida, geometría |
| 4–8 | funciones.py / consola.py | Rangos, factorial, operaciones, repetición, paridad |
| 9–13 | funciones.py / consola.py | Pares, triangulares, factoriales y dominó |
| 14–16 | funciones.py / consola.py | Intervalos e identidad |
| 17–20 | fechas.py / actividades.py | Calendario, días de semana, romanos y tabla de signos |
| 21–29 | numeros.py / actividades.py | Promedios, divisores, contraseñas ficticias, acumuladores y exámenes |
| 30 | cadenas.py | Recortes y reflexión |
| 31–32 | cadenas.py | Inserciones y reemplazos limitados |
| 33–36 | cadenas.py | Miles, palabras, vocales, palíndromos, subcadenas |
| 6.8–6.9 (numeración final del PDF) | cadenas.py | Binario y entrada validada |

Quedan cubiertos los ejercicios principales 1–36 y los dos apartados
finales numerados 6.8–6.9: 38 consignas principales con sus subapartados.
Esto completa esta guía identificada, no toda la formación Full Stack.

## Ejecución

Desde esta carpeta, con Python 3.10+:

    python consola.py producto
    python consola.py bloques
    python consola.py triangulares
    python consola.py intervalos
    python consola.py identidad
    python consola.py fechas
    python consola.py examenes
    python consola.py --help

Desde la raíz del repositorio:

    python -m unittest discover -s pruebas -v

## Decisiones de interpretación

- Geometría recibe dimensiones no negativas como precondición.
- La tabla llega a diez; el intervalo de pares incluye ambos extremos.
- El múltiplo inferior es estrictamente menor: 150 da 140.
- Las unidades de un entero negativo ignoran el signo.
- El dominó contiene pares sin repetición, incluido cero.
- Los intervalos normalizan la suma sin limitar las horas a 23.
- Agrupar desde la izquierda (31d) y separar miles desde la derecha (33)
  son operaciones diferentes. Los límites cuentan inserciones/reemplazos.
- Los palíndromos ignoran espacios, signos, mayúsculas y tildes.
- El desplazamiento de vocales conserva el alfabeto sin tilde del enunciado.
- La entrada validada reintenta errores de valor; EOF/cancelación no se ocultan.
- El ordinal del año incluye la fecha: el 1 de enero es 1; los días que
  faltan excluyen el día actual. Entre fechas se devuelve el intervalo
  absoluto, en meses completos y días restantes; aniversarios del 29/2
  o del día 31 se ajustan al último día del mes de destino.
- Romanos usa notación clásica de 1 a 3999. Los signos siguen exactamente
  los límites del PDF (cambio el 21); es una tabla del ejercicio, no una
  afirmación científica.
- La contraseña está inventada y es pública: no debe reutilizarse para
  una cuenta real. La función permite las cuatro variantes de la consigna;
  la consola muestra la variante de tres intentos y espera creciente.
- Los múltiplos son positivos y estrictamente menores que el límite;
  el cero no se cuenta. while visita sólo los múltiplos; for examina
  cada entero, por lo que realiza más operaciones.
- Perfectos y amigos se buscan sin suponer que todos los perfectos son
  pares: divisores hasta la raíz, parejas sin duplicados y caché acotada.
  Pedir muchos resultados puede ser costoso; no es una búsqueda masiva.
- Con una sucesión vacía se informa «sin datos» para el promedio; -1 sólo
  controla la entrada. Los exámenes validan total, porcentaje y resueltos.
