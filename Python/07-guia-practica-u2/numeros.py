"""U2 21–29: acumuladores, divisores y evaluación; propuestas nuevas de 2026."""
from functools import lru_cache
from math import isfinite, isqrt


def promedio(valores):
    valores = list(valores)
    if not valores or any(not isfinite(x) for x in valores):
        raise ValueError("Se requiere al menos un valor finito")
    return sum(valores)/len(valores)


def factores_primos(numero):
    if numero < 1:
        raise ValueError("Se requiere un entero positivo")
    factores, divisor = [], 2
    while divisor*divisor <= numero:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    if numero > 1:
        factores.append(numero)
    return factores


@lru_cache(maxsize=32768)
def suma_divisores(numero):
    if numero < 1:
        raise ValueError("Se requiere un entero positivo")
    if numero == 1:
        return 0
    suma = 1
    for divisor in range(2,isqrt(numero)+1):
        if numero % divisor == 0:
            suma += divisor
            cociente = numero//divisor
            if cociente != divisor:
                suma += cociente
    return suma


def perfectos(cantidad):
    if cantidad < 0:
        raise ValueError("Cantidad no negativa")
    resultado, numero = [], 2
    while len(resultado) < cantidad:
        if suma_divisores(numero) == numero:
            resultado.append(numero)
        numero += 1
    return resultado


def amigos(cantidad):
    if cantidad < 0:
        raise ValueError("Cantidad no negativa")
    resultado, numero = [], 2
    while len(resultado) < cantidad:
        otro = suma_divisores(numero)
        if otro > numero and suma_divisores(otro) == numero:
            resultado.append((numero, otro))
        numero += 1
    return resultado


def resumen_naturales(valores):
    valores = list(valores)
    if any(x < 0 for x in valores):
        raise ValueError("El centinela se procesa en la entrada, no como dato")
    return len(valores), sum(valores), promedio(valores) if valores else None


def multiplos_for(primero, segundo):
    if primero <= 0 or segundo < 0:
        raise ValueError("Base positiva y límite no negativo")
    return sum(n % primero == 0 for n in range(primero,segundo))


def multiplos_while(primero, segundo):
    if primero <= 0 or segundo < 0:
        raise ValueError("Base positiva y límite no negativo")
    cantidad, multiplo = 0, primero
    while multiplo < segundo:
        cantidad += 1
        multiplo += primero
    return cantidad


def primos_hasta(limite):
    if limite < 0:
        raise ValueError("Límite no negativo")
    return [n for n in range(2,limite+1)
            if all(n % divisor != 0 for divisor in range(2,isqrt(n)+1))]


def contiene_digito(digito, numero):
    if not 0 <= digito <= 9 or numero < 0:
        raise ValueError("Dígito de 0 a 9 y número natural")
    if numero == 0:
        return digito == 0
    while numero:
        if numero % 10 == digito:
            return True
        numero //= 10
    return False


def evaluar_examen(total, umbral, resueltos):
    if total <= 0 or not isfinite(umbral) or not 0 <= umbral <= 100 or not 0 <= resueltos <= total:
        raise ValueError("Cantidad o porcentaje fuera de rango")
    porcentaje = 100*resueltos/total
    return porcentaje, porcentaje >= umbral
