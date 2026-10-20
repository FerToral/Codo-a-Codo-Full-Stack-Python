# Codo a Codo — Full Stack Python

Prácticas de la formación Full Stack de Codo a Codo: fundamentos de Python,
guías de ejercicios y una entrega web de astronomía con HTML/CSS.

## Prácticas web

- [Astronomía](Web/Trabajos-Practicos/Astronomia/): seis páginas, listas,
  tablas y formulario local. Se conserva la identidad histórica TP N.º 2;
  no se afirma que sea el final Django ni que equivalga al integrador TP06.
- [Letra del DNI](Web/Practicas/Letra-DNI/): versión de navegador de U1/22.
  El cálculo corresponde al documento español, no al DNI argentino.

## Recorrido de Python

| Módulo | Contenido | Ejercicios |
| --- | --- | ---: |
| [Ejercicios adicionales U1](Python/00-guia-practica-u1) | Entrada/salida, decisiones y ciclos | 24 consignas utilizables; 25 con alternativa explícita para un dibujo ausente |
| [Funciones](Python/01-funciones) | Parámetros y valores de retorno | 1 |
| [Colecciones](Python/02-colecciones) | Listas, tuplas, diccionarios y captura de datos | 4 |
| [Condicionales](Python/03-condicionales) | Evaluación, selección, máximo, calculadora y media | 6 |
| [Bucles y generadores](Python/04-bucles-y-generadores) | Acumulación, búsqueda y `yield` | 3 |
| [Excepciones](Python/05-excepciones) | Raíz cuadrada y entradas inválidas | 1 |
| [Programación orientada a objetos](Python/06-poo/Banco) | Clases abstractas, herencia, polimorfismo y gestión de clientes | 1 actividad integradora |
| [Guía práctica U2](Python/07-guia-practica-u2) | Funciones, fechas, números, consola y cadenas | 38 consignas principales con subapartados; propuestas nuevas |

Cada archivo es una práctica independiente. Algunos conservan comentarios y variantes del momento de aprendizaje. Las versiones anteriores se conservan en el respaldo histórico; la correspondencia de nombres está en [procedencia](docs/procedencia.md).

La actividad POO Banco y las resoluciones de U2 son propuestas nuevas basadas en consignas del material compartido; se distinguen de los quince scripts históricos. U2 conserva la numeración de sus ejercicios y sus decisiones de interpretación. No son el proyecto final de Full Stack ni recuperaciones de entregas personales antiguas.

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

El material relacionado abarca HTML/CSS, Bootstrap, JavaScript, Vue, bases
de datos, Python y Django. El [índice del material](docs/material-de-la-cursada.md)
mantiene los enlaces entre ejercicios y contenidos. Esta colección cubre
las guías Python y la entrega web identificada; no se presenta como todas
las prácticas de SQL/Django ni como recuperación del final personal.

Los scripts pertenecen a Codo a Codo según la identificación de su autor. Sus fechas históricas de marzo de 2020 preceden al cronograma agosto–diciembre de 2020 de la carpeta compartida: la edición y las clases exactas de estas prácticas siguen pendientes de correlación documental. No se atribuye una clase concreta basándose únicamente en la similitud de temas.

## Comportamientos revisados

La calculadora usa operandos enteros como en el ejercicio original y conserva su precisión en suma, resta y multiplicación. La división utiliza el resultado de la división real de Python.

El máximo verifica ambas notas en `[0, 10]`, la calculadora informa la división por cero y las operaciones desconocidas, la media consulta tres valores una sola vez y la raíz también captura errores al convertir el texto ingresado. La media conserva el intervalo `(0, 10]` del código guardado, porque no se recuperó su consigna específica. Las [pruebas](pruebas/test_python.py) incluyen regresiones de estos casos y una ejecución de los quince scripts.
