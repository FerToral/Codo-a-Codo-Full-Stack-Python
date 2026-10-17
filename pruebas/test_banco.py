"""Comprueba el modelo real de la práctica POO; sin servicios ni datos reales."""
from contextlib import redirect_stdout
from decimal import Decimal
from io import StringIO
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PRACTICA = ROOT / "Python/06-poo/Banco"
with patch.object(sys, "path", [str(PRACTICA)] + sys.path):
    import banco
    from cliente import Cliente, ClienteEstandar, ClienteGold

class PracticaBanco(unittest.TestCase):
    def test_cliente_es_abstracto(self):
        with self.assertRaises(TypeError):
            Cliente("Ejemplo")

    def test_estandar_decimal_y_saldo_no_negativo(self):
        cliente = ClienteEstandar("Ana")
        cliente.depositar("0.10")
        cliente.depositar("0.20")
        self.assertEqual(cliente.saldo, Decimal("0.30"))
        cliente.extraer("0.30")
        self.assertEqual(cliente.saldo, 0)
        with self.assertRaises(ValueError):
            cliente.extraer("0.01")
        self.assertEqual(cliente.saldo, 0)

    def test_gold_limite_reposicion_y_saldo_de_solo_lectura(self):
        cliente = ClienteGold("Bruno", 100)
        cliente.extraer(100)
        self.assertEqual(cliente.saldo, -100)
        with self.assertRaises(ValueError):
            cliente.extraer("0.01")
        cliente.depositar(20)
        self.assertEqual(cliente.saldo, -80)
        with self.assertRaises(AttributeError):
            cliente.saldo = 1000

    def test_importes_invalidos_no_alteran_saldo(self):
        for clase in (ClienteEstandar, ClienteGold):
            cliente = clase("Ana")
            cliente.depositar(100)
            for valor in (-1, 0, "x", "NaN", "Infinity", "0.001"):
                for metodo in (cliente.depositar, cliente.extraer):
                    with self.subTest(clase=clase, valor=valor), self.assertRaises(ValueError):
                        metodo(valor)
                    self.assertEqual(cliente.saldo, 100)

    def test_altas_ids_busqueda_y_listado_polimorfico(self):
        banco1 = banco.Banco("Ejemplo")
        estandar = ClienteEstandar("Ana")
        gold = ClienteGold("Bruno", 50)
        a, b = banco1.cargar_cliente(estandar), banco1.cargar_cliente(gold)
        self.assertEqual((a,b), (1,2))
        self.assertIs(banco1.buscar_cliente(a), estandar)
        salida = StringIO()
        with redirect_stdout(salida):
            banco1.listar_clientes()
        self.assertEqual(len(salida.getvalue().splitlines()), 2)
        self.assertNotIn("descubierto", salida.getvalue().splitlines()[0])
        self.assertIn("descubierto", salida.getvalue().splitlines()[1])
        self.assertEqual(str(banco1), salida.getvalue().strip())

    def test_modificacion_baja_sin_reutilizar_identificadores(self):
        entidad = banco.Banco("Ejemplo")
        a = entidad.cargar_cliente(ClienteEstandar("Ana"))
        entidad.modificar_cliente(a, "Ana Ejemplo")
        self.assertEqual(entidad.buscar_cliente(a).nombre, "Ana Ejemplo")
        eliminado = entidad.eliminar_cliente(a)
        self.assertEqual(eliminado.nombre, "Ana Ejemplo")
        with self.assertRaises(KeyError):
            entidad.buscar_cliente(a)
        b = entidad.cargar_cliente(ClienteEstandar("Clara"))
        self.assertGreater(b, a)
        copia = entidad.clientes
        copia.clear()
        self.assertEqual(len(entidad.clientes), 1)

    def test_nombres_y_duplicados(self):
        with self.assertRaises(ValueError):
            ClienteEstandar(" ")
        entidad = banco.Banco("Ejemplo")
        cliente = ClienteEstandar("Ana")
        entidad.cargar_cliente(cliente)
        with self.assertRaises(ValueError):
            entidad.cargar_cliente(cliente)
        with self.assertRaises(TypeError):
            entidad.cargar_cliente("Ana")
        with self.assertRaises(ValueError):
            entidad.modificar_cliente(1, " ")
        self.assertEqual(cliente.nombre, "Ana")

    def test_demo_ejecutable_y_sin_efectos_al_importar(self):
        importacion = subprocess.run([sys.executable, "-c", "import banco"], cwd=PRACTICA,
                                    capture_output=True, text=True, check=True)
        self.assertEqual(importacion.stdout, "")
        salida = subprocess.run([sys.executable, str(PRACTICA/"banco.py")],
                                capture_output=True, text=True, check=True)
        self.assertEqual(len(salida.stdout.splitlines()), 2)
        self.assertIn("40.10", salida.stdout)
        self.assertIn("-25.50", salida.stdout)

if __name__ == "__main__":
    unittest.main()
