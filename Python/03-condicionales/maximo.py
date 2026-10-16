"""Mayor de dos notas en el intervalo [0, 10]."""


def devolver_maximo(nota_1: int, nota_2: int) -> int:
    """Valida ambas notas, aunque la nota inválida sea la menor."""
    if not (0 <= nota_1 <= 10 and 0 <= nota_2 <= 10):
        raise ValueError("Las dos notas deben estar entre 0 y 10.")
    return max(nota_1, nota_2)


def main() -> int:
    try:
        primera = int(input("Ingresar primera nota: "))
        segunda = int(input("Ingresar segunda nota: "))
        resultado = devolver_maximo(primera, segunda)
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return 1
    print("El valor máximo es:", resultado)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
