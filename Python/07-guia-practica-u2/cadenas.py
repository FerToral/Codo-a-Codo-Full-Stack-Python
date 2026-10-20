"""U2, ejercicios 30–36 y 6.8/6.9. Soluciones nuevas con contratos explícitos."""

import unicodedata


def recortes(cadena):
    return cadena[:2], cadena[-3:], cadena[::2], cadena[::-1], cadena+cadena[::-1]


def _limite(maximo):
    if maximo is not None and (not isinstance(maximo, int) or maximo < 0):
        raise ValueError("El límite debe ser entero no negativo")
    return maximo


def intercalar(cadena, caracter, maximo=None):
    _limite(maximo)
    partes = []
    for i, letra in enumerate(cadena):
        if i and (maximo is None or i <= maximo):
            partes.append(caracter)
        partes.append(letra)
    return "".join(partes)


def reemplazar_espacios(cadena, caracter, maximo=None):
    _limite(maximo)
    return cadena.replace(" ", caracter, -1 if maximo is None else maximo)


def reemplazar_digitos(cadena, caracter, maximo=None):
    _limite(maximo)
    partes, cambios = [], 0
    for letra in cadena:
        if letra.isdecimal() and (maximo is None or cambios < maximo):
            partes.append(caracter)
            cambios += 1
        else:
            partes.append(letra)
    return "".join(partes)


def agrupar_tres(cadena, separador=".", maximo=None):
    """Ej.31d agrupa desde la izquierda, incluso el último grupo corto."""
    _limite(maximo)
    partes, cambios = [], 0
    for i, letra in enumerate(cadena):
        if i and i % 3 == 0 and (maximo is None or cambios < maximo):
            partes.append(separador)
            cambios += 1
        partes.append(letra)
    return "".join(partes)


def miles(numero):
    """Ej.33 agrupa desde la derecha, preservando signo y ceros iniciales."""
    signo = numero[:1] if numero[:1] in ("+", "-") else ""
    digitos = numero[len(signo):]
    if not digitos or not digitos.isascii() or not digitos.isdecimal():
        raise ValueError("Se requiere una cadena de dígitos decimales")
    inicio = len(digitos) % 3 or 3
    grupos = [digitos[:inicio]]
    grupos.extend(digitos[i:i+3] for i in range(inicio, len(digitos), 3))
    return signo + ".".join(grupos)


def iniciales(cadena):
    return "".join(palabra[0] for palabra in cadena.split())


def capitalizar(cadena):
    return " ".join(p[:1].upper()+p[1:] for p in cadena.split())


def palabras_con_a(cadena):
    return " ".join(p for p in cadena.split() if p.casefold().startswith("a"))


def _base(letra):
    return "".join(c for c in unicodedata.normalize("NFD", letra.casefold())
                   if not unicodedata.combining(c))


def consonantes(cadena):
    return "".join(c for c in cadena if c.isalpha() and _base(c) not in "aeiou")


def vocales(cadena):
    # Se conservan los espacios, como en el ejemplo 'i ooae' de la guía.
    return "".join(c for c in cadena if c.isspace() or _base(c) in "aeiou")


def siguiente_vocal(cadena):
    minusculas = str.maketrans("aeiou", "eioua")
    mayusculas = str.maketrans("AEIOU", "EIOUA")
    return cadena.translate(minusculas).translate(mayusculas)


def palindromo(cadena):
    normalizada = "".join(_base(c) for c in cadena if c.isalnum())
    return normalizada == normalizada[::-1]


def es_subcadena(primera, segunda):
    return segunda in primera


def anterior(primera, segunda):
    """Orden lexicográfico Unicode de Python, no orden de diccionario regional."""
    return min(primera, segunda)


def binario_a_decimal(cadena):
    if not cadena or any(c not in "01" for c in cadena):
        raise ValueError("Se requiere una cadena no vacía de ceros y unos")
    valor = 0
    for bit in cadena:
        valor = valor*2 + int(bit)
    return valor


def pedir_entero(mensaje, minimo, maximo, entrada=input, salida=print):
    if minimo > maximo:
        raise ValueError("El mínimo no puede superar el máximo")
    while True:
        try:
            valor = int(entrada(f"{mensaje} [{minimo}..{maximo}]: "))
        except ValueError:
            salida(f"Por favor ingresa un número entre {minimo} y {maximo}.")
            continue
        if minimo <= valor <= maximo:
            return valor
        salida(f"Por favor ingresa un número entre {minimo} y {maximo}.")
