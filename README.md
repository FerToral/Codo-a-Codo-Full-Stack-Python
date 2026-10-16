# Codo a Codo — Full Stack Python

Ejercicios de Python de la formación Full Stack de Codo a Codo: funciones, colecciones, condicionales, bucles, generadores y excepciones.

## Recorrido de Python

| Módulo | Contenido | Ejercicios |
| --- | --- | ---: |
| [Funciones](Python/01-funciones) | Parámetros y valores de retorno | 1 |
| [Colecciones](Python/02-colecciones) | Listas, tuplas, diccionarios y captura de datos | 4 |
| [Condicionales](Python/03-condicionales) | Evaluación, selección, máximo, calculadora y media | 6 |
| [Bucles y generadores](Python/04-bucles-y-generadores) | Acumulación, búsqueda y `yield` | 3 |
| [Excepciones](Python/05-excepciones) | Raíz cuadrada y entradas inválidas | 1 |

Cada archivo es una práctica independiente. Algunos conservan comentarios y variantes del momento de aprendizaje. Las versiones anteriores se conservan en el respaldo histórico; la correspondencia de nombres está en [procedencia](docs/procedencia.md).

## Ejecución

Se requiere Python 3.10 o posterior, sin bibliotecas adicionales. Desde la carpeta principal:

```console
python Python/03-condicionales/maximo.py
python Python/03-condicionales/calculadora.py
python Python/05-excepciones/raiz_cuadrada.py
python -m unittest discover -s pruebas -v
```

Los ejemplos de máximo, calculadora, media y raíz tienen funciones reutilizables y un punto de entrada de consola. Las entradas inválidas muestran un mensaje y devuelven el código de salida 1. El resto de las prácticas sigue el formato de scripts de clase.

## La formación Full Stack

El material relacionado abarca HTML/CSS, Bootstrap, JavaScript, Vue, bases de datos, Python y Django. El [índice del material](docs/material-de-la-cursada.md) mantiene los enlaces entre ejercicios y contenidos. Este conjunto de prácticas cubre Python; los proyectos web y de bases de datos tienen que identificarse por sus propias entregas.

Los scripts pertenecen a Codo a Codo según la identificación de su autor. Sus fechas históricas de marzo de 2020 preceden al cronograma agosto–diciembre de 2020 de la carpeta compartida: la edición y las clases exactas de estas prácticas siguen pendientes de correlación documental. No se atribuye una clase concreta basándose únicamente en la similitud de temas.

## Comportamientos revisados

La calculadora usa operandos enteros como en el ejercicio original y conserva su precisión en suma, resta y multiplicación. La división utiliza el resultado de la división real de Python.

El máximo verifica ambas notas en `[0, 10]`, la calculadora informa la división por cero y las operaciones desconocidas, la media consulta tres valores una sola vez y la raíz también captura errores al convertir el texto ingresado. La media conserva el intervalo `(0, 10]` del código guardado, porque no se recuperó su consigna específica. Las [pruebas](pruebas/test_python.py) incluyen regresiones de estos casos y una ejecución de los quince scripts.
