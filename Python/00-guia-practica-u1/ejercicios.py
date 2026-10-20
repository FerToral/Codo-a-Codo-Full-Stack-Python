"""Guía adicional U1: funciones y consola. Resoluciones nuevas de 2026."""
import argparse
from math import isfinite, isqrt


def vocales(frase):
    # Comparación sin distinguir mayúsculas; las letras acentuadas son otras.
    return {v: frase.lower().count(v) for v in "aeiou"}


def divisores(numero):
    if numero == 0:
        raise ValueError("Cero no tiene una lista finita de divisores")
    numero = abs(numero)
    return [d for d in range(1,numero+1) if numero % d == 0]


def es_primo(numero):
    return numero >= 2 and all(numero % d for d in range(2,isqrt(numero)+1))


def calificacion(nota):
    if not isfinite(nota) or not 0 <= nota <= 10:
        raise ValueError("La nota debe estar entre 0 y 10")
    for limite, nombre in ((3,"Muy deficiente"),(5,"Insuficiente"),(6,"Suficiente"),
                            (7,"Bien"),(9,"Notable")):
        if nota < limite:
            return nombre
    return "Sobresaliente"


def letra_dni(numero):
    if not 0 <= numero <= 99999999:
        raise ValueError("Número entre 0 y 99999999")
    return "TRWAGMYFPDXBNJZSQVHLCKE"[numero % 23]


def piramide(numero, inversa=False, acumulativa=False):
    if not 1 <= numero <= 50:
        raise ValueError("Altura de 1 a 50")
    indices = range(numero,0,-1) if inversa else range(1,numero+1)
    return ["".join(str(x) for x in range(1,i+1)) if acumulativa else str(i)*i for i in indices]


def marcas_multiplos(limite=500):
    lineas = []
    for n in range(1,limite+1):
        marcas = [f"Múltiplo de {d}" for d in (4,9) if n % d == 0]
        lineas.append(str(n)+(" ("+", ".join(marcas)+")" if marcas else ""))
        if n % 5 == 0:
            lineas.append("—"*24)
    return lineas


def hasta_cancelar(entrada, texto):
    """EOF termina; la palabra exacta cancelar representa el botón de la guía."""
    while True:
        try:
            valor = entrada(texto)
        except EOFError:
            return
        if valor.strip().lower() == "cancelar":
            return
        yield valor


def numero_real(texto):
    numero = float(texto)
    if not isfinite(numero):
        raise ValueError("Se requiere un número finito")
    return numero


def ejecutar(ejercicio, entrada=input, salida=print):
    def entero(texto="Entero"):
        return int(entrada(texto+": "))
    def real():
        return numero_real(entrada("Número: "))
    if ejercicio == 1:
        salida("Hello World")
    elif ejercicio == 2:
        salida(3+5)
    elif ejercicio == 3:
        salida("Hola",entrada("Nombre: "))
    elif ejercicio == 4:
        salida(real()+real())
    elif ejercicio in (5,6):
        salida(max(real() for _ in range(2 if ejercicio == 5 else 3)))
    elif ejercicio == 7:
        salida(entero() % 2 == 0)
    elif 8 <= ejercicio <= 11:
        frecuencias = vocales(entrada("Frase: "))
        if ejercicio == 8:
            salida(frecuencias["a"])
        elif ejercicio == 9:
            salida(" ".join(v for v,cantidad in frecuencias.items() if cantidad))
        elif ejercicio == 10:
            salida(sum(frecuencias.values()))
        else:
            for v,cantidad in frecuencias.items():
                salida(v,cantidad)
    elif ejercicio in (12,13):
        n = entero()
        encontrados = [d for d in (2,3,5,7) if n % d == 0]
        salida(bool(encontrados)) if ejercicio == 12 else salida(*encontrados)
    elif ejercicio == 14:
        salida(*divisores(entero()))
    elif ejercicio == 15:
        a,b = divisores(entero()),divisores(entero())
        salida(*(d for d in a if d in b))
    elif ejercicio == 16:
        salida(es_primo(entero()))
    elif ejercicio == 17:
        edad = entero("Edad")
        if edad < 0:
            raise ValueError("Edad no negativa")
        salida("Puede conducir" if edad > 18 else "No supera los 18 años")
    elif ejercicio == 18:
        salida(calificacion(real()))
    elif ejercicio == 20:
        salida("-".join(hasta_cancelar(entrada,"Texto (cancelar termina): ")))
    elif ejercicio == 21:
        suma = 0
        for valor in hasta_cancelar(entrada,"Número (cancelar termina): "):
            try:
                suma += numero_real(valor)
            except ValueError:
                salida("No es un número válido")
        salida("Suma:",suma)
    elif ejercicio == 22:
        for valor in hasta_cancelar(entrada,"DNI (cancelar termina): "):
            try:
                salida(letra_dni(int(valor)))
            except ValueError:
                salida("DNI inválido")
    elif ejercicio in (23,24,25):
        altura = 30 if ejercicio == 23 else entero("Altura")
        for fila in piramide(altura,inversa=ejercicio==24,acumulativa=ejercicio==25):
            salida(fila)
    elif ejercicio == 26:
        for linea in marcas_multiplos():
            salida(linea)
    else:
        raise ValueError("Ejercicio no identificado en la guía")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ejercicio",type=int,choices=(*range(1,19),*range(20,27)))
    args = parser.parse_args()
    try:
        ejecutar(args.ejercicio)
    except (ValueError,EOFError) as error:
        parser.exit(1,f"Entrada inválida: {error}\n")


if __name__ == "__main__":
    main()
