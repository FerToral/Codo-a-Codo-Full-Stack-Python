"""Práctica POO: propuesta de estudio de 2026, basada en la consigna CaC.
Datos ficticios; no es software bancario ni autenticación real.
"""
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


def importe(valor, *, permitir_cero=False):
    try:
        numero = Decimal(str(valor))
        if not numero.is_finite():
            raise ValueError("El importe debe ser finito")
        centavos = numero.quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError) as error:
        raise ValueError("Importe inválido") from error
    if numero != centavos or numero < 0 or (numero == 0 and not permitir_cero):
        raise ValueError("Se requiere importe positivo de hasta dos decimales")
    return centavos


class Cliente(ABC):
    def __init__(self, nombre):
        self.establecer_nombre(nombre)
        self._saldo = Decimal("0.00")

    def establecer_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre no vacío")
        self.nombre = nombre.strip()

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"{self.nombre} | saldo: {self.saldo:.2f}"

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def extraer(self, valor):
        pass

    def _depositar(self, valor):
        # Un depósito puede reducir una deuda Gold sin volver positivo el saldo.
        self._saldo += importe(valor)

    def _extraer(self, valor, limite):
        monto = importe(valor)
        if self._saldo - monto < -limite:
            raise ValueError("Saldo disponible insuficiente")
        self._saldo -= monto


class ClienteEstandar(Cliente):
    def depositar(self, valor):
        self._depositar(valor)

    def extraer(self, valor):
        self._extraer(valor, Decimal("0"))


class ClienteGold(Cliente):
    def __init__(self, nombre, descubierto=0):
        super().__init__(nombre)
        self._descubierto = importe(descubierto, permitir_cero=True)

    @property
    def descubierto(self):
        return self._descubierto

    def depositar(self, valor):
        self._depositar(valor)

    def extraer(self, valor):
        self._extraer(valor, self.descubierto)

    def __str__(self):
        return f"{super().__str__()} | descubierto: {self.descubierto:.2f}"
