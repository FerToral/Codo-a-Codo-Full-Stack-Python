# Python · Ejercicios adicionales U1

Entrada/salida, expresiones, decisiones y ciclos. Cada actividad se ejecuta desde la consola y conserva la numeración de la guía U1.

| Numeración original | Actividad |
|---|---|
| 1–7 | Salidas, saludo, suma, máximos, paridad |
| 8–11 | Vocales y frecuencias |
| 12–16 | Divisibilidad, divisores comunes, primalidad |
| 17–18 | Edad y calificación |
| 20–22 | Entrada repetida, suma validada, letra del DNI español |
| 23–24 | Pirámides de repetición, ascendente e inversa |
| 25 | Enunciado incompleto: propuesta alternativa de pirámide acumulativa |
| 26 | Múltiplos de 4 y 9 con separadores |

El documento no contiene el número 19. El 25 anuncia «la pirámide
siguiente», pero no muestra el dibujo, tampoco al renderizar la página:
se incluye una variante acumulativa para practicar ese tipo de patrón. Hay 24 consignas utilizables y esa alternativa explícita.

## Ejecución y convenciones

    python ejercicios.py 8
    python ejercicios.py 21
    python ejercicios.py 25

La guía está guardada en Python pero reutiliza expresiones de navegador
(alert, cancelar, página/script). Aquí se adaptan al terminal: cancelar
o EOF terminan las entradas repetidas; los errores del 21/22 se informan
y permiten reintentar. La versión web del 22 está en
[Web/Practicas/Letra-DNI](../../Web/Practicas/Letra-DNI/).
No se trata del DNI argentino ni de una validación de identidad.

Se conserva el criterio literal «mayor de 18» del ejercicio 17 (no es
asesoramiento sobre edad legal). Los intervalos de notas se interpretan
cerrados a izquierda y abiertos a derecha, con 10 incluido en la última
categoría. Se normalizan mayúsculas para vocales, no tildes. En el 9 cada
vocal presente se muestra una vez en orden a/e/i/o/u. Los divisores son
positivos; cero se rechaza porque su lista no sería finita.
