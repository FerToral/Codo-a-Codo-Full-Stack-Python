"""Ejecutables de los ejercicios U2 2, 4, 6, 7, 9–16."""
import argparse
from actividades import ACTIVIDADES, ejecutar as ejecutar_actividad
from funciones import (
    producto, operaciones, tabla, repetir_palabra, pares_entre, triangulares,
    factoriales, domino, sumar_intervalos, identidad,
)


def ejecutar(actividad, entrada=input, salida=print):
    if actividad == "producto":
        salida(producto(float(entrada("Primer número: ")), float(entrada("Segundo número: "))))
    elif actividad == "bloques":
        for i in range(5):
            salida(i*i)
        for i in range(2, 6):
            salida(i, 2**i)
    elif actividad == "operaciones":
        valores = operaciones(float(entrada("Primero: ")), float(entrada("Segundo: ")))
        for nombre, valor in valores.items():
            salida(nombre, "indefinida (división por cero)" if valor is None else valor)
    elif actividad == "tabla":
        for i, valor in tabla(int(entrada("Número: "))):
            salida(i, valor)
    elif actividad == "palabra":
        salida(repetir_palabra(entrada("Palabra: ")))
    elif actividad == "pares":
        for n in pares_entre(int(entrada("Desde: ")), int(entrada("Hasta: "))):
            salida(n)
    elif actividad == "triangulares":
        for i, valor in triangulares(int(entrada("Cantidad: "))):
            salida(f"{i} - {valor}")
    elif actividad == "factoriales":
        cantidad = int(entrada("Cantidad: "))
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        valores = [int(entrada("Entero no negativo: ")) for _ in range(cantidad)]
        for i, valor in factoriales(valores):
            salida(i, valor)
    elif actividad == "domino":
        for ficha in domino():
            salida(*ficha)
    elif actividad == "domino-n":
        for ficha in domino(int(entrada("Máximo: "))):
            salida(*ficha)
    elif actividad == "intervalos":
        intervalos = [tuple(int(entrada(campo+": ")) for campo in ("Horas","Minutos","Segundos"))
                      for _ in range(2)]
        salida(*sumar_intervalos(*intervalos))
    elif actividad == "identidad":
        for fila in identidad(int(entrada("Dimensión: "))):
            salida(*fila)
    elif actividad in ACTIVIDADES:
        ejecutar_actividad(actividad,entrada,salida)
    else:
        raise ValueError("Actividad desconocida")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actividad", choices=(
        "producto","bloques","operaciones","tabla","palabra","pares","triangulares",
        "factoriales","domino","domino-n","intervalos","identidad",
    ) + ACTIVIDADES)
    args = parser.parse_args()
    try:
        ejecutar(args.actividad)
    except (ValueError, EOFError) as error:
        parser.exit(1, f"Entrada inválida: {error}\n")


if __name__ == "__main__":
    main()
