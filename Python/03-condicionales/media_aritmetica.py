"""Media de tres notas; conserva el dominio (0, 10] del ejercicio guardado."""


def media_aritmetica(primera: float, segunda: float, tercera: float) -> float:
    notas = (primera, segunda, tercera)
    if not all(0 < nota <= 10 for nota in notas):
        raise ValueError("Las tres notas deben ser mayores que 0 y no superar 10.")
    return sum(notas) / len(notas)


def main() -> int:
    try:
        primera = float(input("Ingresar primera nota: "))
        segunda = float(input("Ingresar segunda nota: "))
        tercera = float(input("Ingresar tercera nota: "))
        resultado = media_aritmetica(primera, segunda, tercera)
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return 1
    print("Media aritmética:", resultado)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
