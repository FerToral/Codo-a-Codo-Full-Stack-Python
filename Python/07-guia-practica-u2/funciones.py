"""U2, ejercicios 1–16: propuesta de resolución de 2026, no entrega histórica."""

import math


def producto(a, b):
    return a * b


def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)


def area_rectangulo(base, altura):
    return base * altura


def perimetro_circulo(radio):
    return 2 * math.pi * radio


def area_circulo(radio):
    return math.pi * radio**2


def volumen_esfera(radio):
    return 4 * math.pi * radio**3 / 3


def hipotenusa(a, b):
    return math.hypot(a, b)


def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("El factorial requiere un entero no negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def operaciones(a, b):
    """La división por cero se informa sin perder las otras operaciones."""
    return {"suma": a+b, "resta": a-b, "producto": a*b,
            "division": a/b if b != 0 else None}


def tabla(n):
    return [(i, n*i) for i in range(1, 11)]


def repetir_palabra(palabra):
    return " ".join([palabra] * 1000)


def es_impar(n):
    return n % 2


def es_par(n):
    return 1 - es_impar(n)


def unidades(n):
    return abs(n) % 10


def multiplo_diez_inferior(n):
    """'Inferior' se interpreta estrictamente: para 150 devuelve 140."""
    return ((n - 1) // 10) * 10


def pares_entre(a, b):
    """Intervalo cerrado; si los extremos están invertidos, se ordenan."""
    a, b = sorted((a, b))
    return list(range(a + a % 2, b + 1, 2))


def triangulares(n):
    if n < 0:
        raise ValueError("La cantidad no puede ser negativa")
    return [(i, i*(i+1)//2) for i in range(1, n+1)]


def factoriales(valores):
    return [(i, factorial(n)) for i, n in enumerate(valores, start=1)]


def domino(n=6):
    if n < 0:
        raise ValueError("El máximo no puede ser negativo")
    return [(a, b) for a in range(n+1) for b in range(a, n+1)]


def a_segundos(horas, minutos, segundos):
    if horas < 0 or not 0 <= minutos < 60 or not 0 <= segundos < 60:
        raise ValueError("Intervalo inválido")
    return horas*3600 + minutos*60 + segundos


def a_hms(segundos):
    if not isinstance(segundos, int) or segundos < 0:
        raise ValueError("Se requieren segundos enteros no negativos")
    horas, resto = divmod(segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return horas, minutos, segundos


def sumar_intervalos(primero, segundo):
    return a_hms(a_segundos(*primero) + a_segundos(*segundo))


def identidad(n):
    if n < 0:
        raise ValueError("La dimensión no puede ser negativa")
    return [[int(fila == columna) for columna in range(n)] for fila in range(n)]
