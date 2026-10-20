"""Entradas/salidas U2 17–29; contraseña ficticia, sin autenticación real."""
from time import sleep
from fechas import (
    exigir_fecha, es_bisiesto, dias_del_mes, dias_hasta_fin_de_mes,
    dias_hasta_fin_de_anio, dias_transcurridos, tiempo_entre_fechas,
    dia_de_semana, romano, signo,
)
from numeros import (
    promedio, factores_primos, perfectos, amigos, resumen_naturales,
    multiplos_for, multiplos_while, primos_hasta, contiene_digito, evaluar_examen,
)

ACTIVIDADES = ("fechas","semana","romano","signo","promedio","factores","clave",
               "perfectos","amigos","sucesion","multiplos","primos","digito","examenes")
CLAVE_DEMOSTRACION = "clave-de-ejemplo"


def verificar_clave(clave, intentos=None, pausa=0, entrada=input, esperar=sleep):
    """23a: ilimitado; 23b/d: límite y bool; 23c: espera creciente tras fallos."""
    if intentos is not None and intentos < 0 or pausa < 0:
        raise ValueError("Intentos y pausa no negativos")
    fallos = 0
    while intentos is None or fallos < intentos:
        if entrada("Contraseña de demostración: ") == clave:
            return True
        fallos += 1
        if pausa and (intentos is None or fallos < intentos):
            esperar(pausa*fallos)
    return False


def ejecutar(actividad, entrada=input, salida=print):
    def entero(texto):
        return int(entrada(texto+": "))

    if actividad == "fechas":
        primera = tuple(entero(campo) for campo in ("Día","Mes","Año"))
        dia, mes, anio = primera
        exigir_fecha(*primera)
        salida("Bisiesto:",es_bisiesto(anio),"Días del mes:",dias_del_mes(mes,anio))
        salida("Hasta fin de mes:",dias_hasta_fin_de_mes(*primera))
        salida("Hasta fin de año:",dias_hasta_fin_de_anio(*primera))
        salida("Día del año:",dias_transcurridos(*primera))
        segunda = tuple(entero(campo) for campo in ("Segundo día","Segundo mes","Segundo año"))
        salida("Años, meses, días:",*tiempo_entre_fechas(primera,segunda))
    elif actividad == "semana":
        salida(dia_de_semana(entero("Día del año")))
    elif actividad == "romano":
        salida(romano(entero("Año")))
    elif actividad == "signo":
        salida(signo(entero("Día"),entero("Mes")))
    elif actividad == "promedio":
        notas = [float(entrada("Nota: "))]
        while entrada("¿Otra nota? [s/n]: ").strip().lower() == "s":
            notas.append(float(entrada("Nota: ")))
        salida("Promedio:",promedio(notas))
    elif actividad == "factores":
        salida(*factores_primos(entero("Entero positivo")))
    elif actividad == "clave":
        salida("Clave ficticia del ejercicio:",CLAVE_DEMOSTRACION)
        salida(verificar_clave(CLAVE_DEMOSTRACION,intentos=3,pausa=1,entrada=entrada))
    elif actividad in {"perfectos","amigos"}:
        cantidad = entero("Cantidad (la búsqueda exhaustiva puede ser lenta)")
        salida(*(perfectos(cantidad) if actividad == "perfectos" else amigos(cantidad)))
    elif actividad == "sucesion":
        valores = []
        while True:
            numero = entero("Natural (-1 termina)")
            if numero == -1:
                break
            if numero < 0:
                raise ValueError("Sólo naturales o -1")
            valores.append(numero)
        cantidad, suma, media = resumen_naturales(valores)
        salida("Cantidad:",cantidad,"Suma:",suma,"Promedio:",media if media is not None else "sin datos")
    elif actividad == "multiplos":
        a,b = entero("Base positiva"),entero("Límite exclusivo")
        salida("for:",multiplos_for(a,b),"while:",multiplos_while(a,b))
    elif actividad == "primos":
        salida(*primos_hasta(entero("Hasta")))
    elif actividad == "digito":
        salida(contiene_digito(entero("Dígito"),entero("Natural")))
    elif actividad == "examenes":
        total, umbral = entero("Total de ejercicios"),float(entrada("Porcentaje para aprobar: "))
        evaluar_examen(total,umbral,0)
        while True:
            resueltos = entero("Resueltos (-1 termina)")
            if resueltos == -1:
                break
            porcentaje, aprobado = evaluar_examen(total,umbral,resueltos)
            salida(f"{porcentaje:g}% — {'Aprobado' if aprobado else 'Desaprobado'}")
    else:
        raise ValueError("Actividad desconocida")
