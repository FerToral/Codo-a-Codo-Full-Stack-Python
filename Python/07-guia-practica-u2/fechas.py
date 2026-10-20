"""U2 17–20: calendario gregoriano, romanos y tabla de signos de la guía."""
from datetime import date


def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def dias_del_mes(mes, anio):
    if not 1 <= anio <= 9999 or not 1 <= mes <= 12:
        raise ValueError("Año o mes fuera del calendario admitido")
    return (31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31)[mes-1]


def fecha_valida(dia, mes, anio):
    try:
        return 1 <= dia <= dias_del_mes(mes, anio)
    except ValueError:
        return False


def exigir_fecha(dia, mes, anio):
    if not fecha_valida(dia, mes, anio):
        raise ValueError("Fecha inválida")
    return date(anio, mes, dia)


def dias_hasta_fin_de_mes(dia, mes, anio):
    exigir_fecha(dia, mes, anio)
    return dias_del_mes(mes, anio)-dia


def dias_transcurridos(dia, mes, anio):
    exigir_fecha(dia, mes, anio)
    return sum(dias_del_mes(m, anio) for m in range(1, mes))+dia


def dias_hasta_fin_de_anio(dia, mes, anio):
    return (366 if es_bisiesto(anio) else 365)-dias_transcurridos(dia, mes, anio)


def tiempo_entre_fechas(primera, segunda):
    """Tuplas día/mes/año; intervalo absoluto, meses completos y resto en días."""
    inicio, fin = sorted((exigir_fecha(*primera), exigir_fecha(*segunda)))
    meses = (fin.year-inicio.year)*12+fin.month-inicio.month

    def aniversario(cantidad):
        anio, mes = divmod(inicio.year*12+inicio.month-1+cantidad, 12)
        mes += 1
        return date(anio, mes, min(inicio.day, dias_del_mes(mes, anio)))

    if aniversario(meses) > fin:
        meses -= 1
    return meses//12, meses % 12, (fin-aniversario(meses)).days


def dia_de_semana(numero):
    if not 1 <= numero <= 366:
        raise ValueError("Día del año entre 1 y 366")
    return ("lunes","martes","miércoles","jueves","viernes","sábado","domingo")[(numero-1)%7]


def romano(anio):
    if not 1 <= anio <= 3999:
        raise ValueError("Notación romana clásica: de 1 a 3999")
    resultado = ""
    for valor, simbolo in ((1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),
                           (90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),
                           (5,"V"),(4,"IV"),(1,"I")):
        cantidad, anio = divmod(anio, valor)
        resultado += simbolo*cantidad
    return resultado


def signo(dia, mes):
    exigir_fecha(dia, mes, 2000)  # Admite cumpleaños del 29/2.
    signos = ("Capricornio","Acuario","Piscis","Aries","Tauro","Géminis",
              "Cáncer","Leo","Virgo","Libra","Escorpio","Sagitario")
    # La guía fija todos los cambios el 21, no una efeméride astronómica.
    return signos[(mes-1+(dia >= 21)) % 12]
