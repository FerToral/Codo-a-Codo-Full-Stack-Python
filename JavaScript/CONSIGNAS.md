# Actividades de JavaScript

## Clase 14 · Fundamentos

1–3. Mostrar un saludo con `alert`, escribirlo en el documento y calcular 3 + 5.

4–8. Pedir un nombre, sumar dos valores, comparar dos y tres números y comprobar divisibilidad por dos.

9–12. Contar la letra a, listar vocales presentes, contar todas las vocales y obtener sus frecuencias por separado.

13–17. Comprobar divisibilidad por 2, 3, 5 o 7; listar los divisores que correspondan; obtener divisores positivos, divisores comunes y determinar primalidad.

18–19. Evaluar si una edad es mayor que 18 y clasificar una nota de 0 a 10. Los intervalos de notas se toman cerrados por la izquierda y abiertos por la derecha, con 10 incluido en el último.

20–22. Acumular textos separados por guiones, sumar entradas numéricas rechazando errores y calcular la letra de un DNI español. Cancelar termina la entrada; no equivale a introducir cero. El DNI español no es el documento argentino.

23–26. Dibujar una pirámide de repetición de 1 a 30, una inversa de altura indicada, una acumulativa y un listado de 1 a 500 que señale múltiplos de 4 y 9, separado cada cinco números. El dibujo del ejercicio 25 no aparece en el documento disponible: se trabaja una variante acumulativa identificada como alternativa en el selector.

Las vocales distinguen las tildes del alfabeto a/e/i/o/u. La lista de divisores de cero se rechaza porque no es finita.

## Clase 15 · Funciones

Obtener el máximo de dos valores y el promedio de tres notas. Leer notas hasta el centinela -1 y calcular el promedio; si no hay notas, informar que no hay datos.

Definir siguiente, doble y cuadrado; mostrar sus resultados para un valor; componer el doble del siguiente y su cuadrado. Calcular perímetro y superficie de un cuadrado, y longitud y área de un círculo. Las dimensiones no pueden ser negativas.

`02-funciones/ejercicios.js` contiene las funciones; `demostracion.mjs` muestra su uso, incluida la entrada con centinela.

## Clase 16 · Arrays y cadenas

1. Recorrer todas las edades con `while`.
2. Recorrer con `for` y mostrar sólo edades pares.
3. Encontrar el menor valor sin ordenar el array.
4. Encontrar el mayor valor sin ordenar el array.
5. Obtener el elemento en una posición indicada.
6. Listar una sola vez cada valor repetido, sin modificar el array original.
7. Unir los elementos de un array de colores en una cadena.
8. Invertir los dígitos de un entero.
9. Ordenar alfabéticamente las letras de una palabra.
10. Convertir a mayúscula la inicial de cada palabra.
11. Encontrar la palabra más larga de una frase.

Para el 5 se usa posición inicial 1, como indica el texto de la consigna; su ejemplo numérico no coincide con esa convención. Los repetidos conservan el orden de primera aparición. Si hay empate de longitud, se devuelve la primera palabra. Al invertir un número se conserva el signo y se pierden los ceros iniciales del resultado numérico.

Referencia de clase: ejercicios adicionales de JavaScript de las clases 14 y 16, y práctica de funciones de la clase 15, Codo a Codo Full Stack.
