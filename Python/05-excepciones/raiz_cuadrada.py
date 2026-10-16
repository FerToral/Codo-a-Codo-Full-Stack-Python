"""Excepciones: raíz cuadrada real y validación de la entrada por teclado."""

import math


def calcular_raiz(numero: float) -> float:
    if not math.isfinite(numero) or numero < 0:
        raise ValueError("El número debe ser finito y no negativo.")
    return math.sqrt(numero)


def main() -> int:
    try:
        numero = float(input("Introduce un número: "))
        resultado = calcular_raiz(numero)
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return 1
    print("Resultado:", resultado)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
