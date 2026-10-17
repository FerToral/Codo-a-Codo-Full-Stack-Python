"""Altas, búsqueda, modificación, baja y listado polimórfico; ejercicio CaC."""
from cliente import Cliente, ClienteEstandar, ClienteGold


class Banco:
    def __init__(self, nombre):
        if not nombre.strip():
            raise ValueError("Nombre de banco no vacío")
        self.nombre = nombre.strip()
        self._clientes = []
        self._siguiente_id = 1

    @property
    def clientes(self):
        return list(self._clientes)

    def cargar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Se requiere un Cliente")
        if any(actual is cliente for _, actual in self._clientes):
            raise ValueError("El objeto cliente ya está registrado")
        identificador = self._siguiente_id
        self._siguiente_id += 1
        self._clientes.append((identificador, cliente))
        return identificador

    def buscar_cliente(self, identificador):
        for numero, cliente in self._clientes:
            if numero == identificador:
                return cliente
        raise KeyError(identificador)

    def modificar_cliente(self, identificador, nombre):
        self.buscar_cliente(identificador).establecer_nombre(nombre)

    def eliminar_cliente(self, identificador):
        cliente = self.buscar_cliente(identificador)
        self._clientes = [(n,c) for n,c in self._clientes if n != identificador]
        return cliente

    def listar_clientes(self):
        for identificador, cliente in self._clientes:
            print(f"{identificador}: {cliente}")

    def __str__(self):
        return "\n".join(f"{n}: {c}" for n,c in self._clientes)


def main():
    banco = Banco("Banco de práctica")
    ana = ClienteEstandar("Ana Ejemplo")
    bruno = ClienteGold("Bruno Ejemplo", descubierto=100)
    banco.cargar_cliente(ana)
    banco.cargar_cliente(bruno)
    ana.depositar("50.10")
    ana.extraer("10.00")
    bruno.extraer("25.50")
    banco.listar_clientes()


if __name__ == "__main__":
    main()
