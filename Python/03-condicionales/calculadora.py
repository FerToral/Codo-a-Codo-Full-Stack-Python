"""Calculadora de cuatro operaciones con control de errores de entrada."""

def calcular(primero: int, segundo: int, operacion: str) -> int | float:
    if not (isinstance(primero, int) and isinstance(segundo, int)):
        raise ValueError("Los operandos deben ser números enteros.")
    operacion = operacion.strip().lower()
    if operacion == "suma":
        return primero + segundo
    if operacion == "resta":
        return primero - segundo
    if operacion == "multiplica":
        return primero * segundo
    if operacion == "divide":
        if segundo == 0:
            raise ValueError("No se puede dividir por cero.")
        return primero / segundo
    raise ValueError("Operación no contemplada.")


def main() -> int:
    try:
        primero = int(input("Introduce el primer número: "))
        segundo = int(input("Introduce el segundo número: "))
        operacion = input("Operación (suma, resta, multiplica, divide): ")
        resultado = calcular(primero, segundo, operacion)
    except ValueError as error:
        print(f"Entrada inválida: {error}")
        return 1
    print("Resultado:", resultado)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
