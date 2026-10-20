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
| 30 | cadenas.py | Recortes y reflexión |
| 31–32 | cadenas.py | Inserciones y reemplazos limitados |
| 33–36 | cadenas.py | Miles, palabras, vocales, palíndromos, subcadenas |
| 6.8–6.9 (numeración final del PDF) | cadenas.py | Binario y entrada validada |

Los ejercicios 17–29 siguen pendientes en esta selección. No se declara
completa la guía ni la formación Full Stack.

## Ejecución

Desde esta carpeta, con Python 3.10+:

    python consola.py producto
    python consola.py bloques
    python consola.py triangulares
    python consola.py intervalos
    python consola.py identidad
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
