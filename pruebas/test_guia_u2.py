"""Comprueba las resoluciones nuevas sin sustituir ejercicios históricos."""
from pathlib import Path
import importlib.util
import math
import subprocess
import sys
import unittest
from unittest.mock import patch

RAIZ = Path(__file__).resolve().parents[1]
GUIA = RAIZ / "Python/07-guia-practica-u2"


def cargar(nombre):
    spec = importlib.util.spec_from_file_location("u2_"+nombre, GUIA/(nombre+".py"))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


f, c = cargar("funciones"), cargar("cadenas")
with patch.dict(sys.modules, {"funciones": f}):
    consola = cargar("consola")


class FuncionesU2(unittest.TestCase):
    def test_producto(self):
        self.assertEqual(f.producto(-3, 5), -15)
        self.assertEqual(f.producto(0, 4), 0)

    def test_geometria(self):
        self.assertEqual(f.perimetro_rectangulo(3, 4), 14)
        self.assertEqual(f.area_rectangulo(3, 4), 12)
        self.assertAlmostEqual(f.perimetro_circulo(2), 4*math.pi)
        self.assertAlmostEqual(f.area_circulo(2), 4*math.pi)
        self.assertAlmostEqual(f.volumen_esfera(3), 36*math.pi)
        self.assertEqual(f.hipotenusa(3, 4), 5)
        self.assertEqual(f.area_circulo(0), 0)

    def test_factorial(self):
        for n, esperado in [(0,1),(1,1),(5,120),(10,3628800)]:
            self.assertEqual(f.factorial(n), esperado)
        for n in [-1, 1.5, True]:
            with self.assertRaises(ValueError):
                f.factorial(n)

    def test_operaciones_y_division_cero(self):
        self.assertEqual(f.operaciones(6,2),
                         {"suma":8,"resta":4,"producto":12,"division":3})
        self.assertIsNone(f.operaciones(3,0)["division"])
        self.assertEqual(f.operaciones(3,0)["producto"], 0)

    def test_tabla_y_palabra(self):
        self.assertEqual(f.tabla(3), [(i,3*i) for i in range(1,11)])
        texto = f.repetir_palabra("astronomía")
        self.assertEqual(texto.split(), ["astronomía"]*1000)
        self.assertNotIn("\n", texto)

    def test_paridad_unidades_y_multiplo(self):
        for n in range(-20,21):
            self.assertEqual(f.es_par(n)+f.es_impar(n), 1)
        self.assertEqual(f.unidades(-153), 3)
        for n, esperado in [(153,150),(150,140),(0,-10),(-1,-10),(-10,-20)]:
            self.assertEqual(f.multiplo_diez_inferior(n), esperado)

    def test_pares(self):
        self.assertEqual(f.pares_entre(5,-2), [-2,0,2,4])
        self.assertEqual(f.pares_entre(3,3), [])
        self.assertEqual(f.pares_entre(2,2), [2])

    def test_triangulares_y_factoriales(self):
        self.assertEqual(f.triangulares(5), [(1,1),(2,3),(3,6),(4,10),(5,15)])
        self.assertEqual(f.triangulares(0), [])
        self.assertEqual(f.factoriales([0,3,4]), [(1,1),(2,6),(3,24)])
        with self.assertRaises(ValueError):
            f.triangulares(-1)

    def test_domino_sin_duplicados(self):
        for n in range(8):
            fichas = f.domino(n)
            self.assertEqual(len(fichas), (n+1)*(n+2)//2)
            self.assertEqual(len(fichas), len(set(fichas)))
            self.assertTrue(all(0 <= a <= b <= n for a,b in fichas))
        self.assertEqual(len(f.domino()), 28)
        with self.assertRaises(ValueError):
            f.domino(-1)

    def test_intervalos_reversibles(self):
        for segundos in [0,1,59,60,3599,3600,86400,999999]:
            self.assertEqual(f.a_segundos(*f.a_hms(segundos)), segundos)
        self.assertEqual(f.sumar_intervalos((23,59,59),(0,0,1)), (24,0,0))
        for argumentos in [(-1,0,0),(0,60,0),(0,0,60)]:
            with self.assertRaises(ValueError):
                f.a_segundos(*argumentos)
        with self.assertRaises(ValueError):
            f.a_hms(-1)

    def test_identidad_independencia_filas(self):
        matriz = f.identidad(3)
        self.assertEqual(matriz, [[1,0,0],[0,1,0],[0,0,1]])
        matriz[0][1] = 9
        self.assertEqual(matriz[1], [0,1,0])
        self.assertEqual(f.identidad(0), [])
        with self.assertRaises(ValueError):
            f.identidad(-1)


class CadenasU2(unittest.TestCase):
    def test_recortes(self):
        self.assertEqual(c.recortes("recta"), ("re","cta","rca","atcer","rectaatcer"))
        self.assertEqual(c.recortes(""), ("","","","",""))

    def test_intercalar_y_limites(self):
        self.assertEqual(c.intercalar("separar", ","), "s,e,p,a,r,a,r")
        self.assertEqual(c.intercalar("abcd", "-", 2), "a-b-cd")
        self.assertEqual(c.intercalar("ab", "-", 0), "ab")
        self.assertEqual(c.intercalar("", "-"), "")

    def test_reemplazos(self):
        self.assertEqual(c.reemplazar_espacios("mi archivo de texto.txt","_"),
                         "mi_archivo_de_texto.txt")
        self.assertEqual(c.reemplazar_espacios("a b c","_",1), "a_b c")
        self.assertEqual(c.reemplazar_digitos("su clave es: 1540","X"),
                         "su clave es: XXXX")
        self.assertEqual(c.reemplazar_digitos("1234","X",2), "XX34")
        self.assertEqual(c.reemplazar_digitos("1234","X",0), "1234")

    def test_agrupar_no_es_miles(self):
        self.assertEqual(c.agrupar_tres("2552552550"), "255.255.255.0")
        self.assertEqual(c.agrupar_tres("2552552550", ".", 1), "255.2552550")
        self.assertEqual(c.miles("1234567890"), "1.234.567.890")
        self.assertEqual(c.miles("-1234"), "-1.234")
        self.assertEqual(c.miles("+001234"), "+001.234")
        for valor in ["", "-", "12.3", " 123", "１２"]:
            with self.assertRaises(ValueError):
                c.miles(valor)

    def test_limites_invalidos(self):
        for funcion in [c.intercalar,c.reemplazar_espacios,c.reemplazar_digitos,c.agrupar_tres]:
            with self.assertRaises(ValueError):
                funcion("abc","x",-1)

    def test_palabras(self):
        self.assertEqual(c.iniciales("Universal Serial Bus"), "USB")
        self.assertEqual(c.capitalizar("república argentina"), "República Argentina")
        self.assertEqual(c.palabras_con_a("Antes de ayer"), "Antes ayer")
        self.assertEqual(c.iniciales("  "), "")

    def test_vocales_y_consonantes(self):
        self.assertEqual(c.consonantes("algoritmos"), "lgrtms")
        self.assertEqual(c.vocales("sin consonantes"), "i ooae")
        self.assertEqual(c.siguiente_vocal("vestuario"), "vistaerou")
        self.assertEqual(c.siguiente_vocal("AEIOU"), "EIOUA")
        self.assertEqual(c.consonantes("ÁÉÍÓÚ ñ"), "ñ")

    def test_palindromos(self):
        for valor in ["anita lava la tina", "Ánita, lava la tina!", ""]:
            self.assertTrue(c.palindromo(valor))
        self.assertFalse(c.palindromo("algoritmos"))

    def test_subcadena_y_orden(self):
        self.assertTrue(c.es_subcadena("subcadena","cadena"))
        self.assertTrue(c.es_subcadena("abc",""))
        self.assertFalse(c.es_subcadena("abc","ABC"))
        self.assertEqual(c.anterior("kde","gnome"), "gnome")

    def test_binario(self):
        for n in range(1024):
            self.assertEqual(c.binario_a_decimal(format(n,"b")), n)
        for valor in ["","2"," 01","-01","0b11"]:
            with self.assertRaises(ValueError):
                c.binario_a_decimal(valor)

    def test_pedir_entero_reintentos(self):
        entradas = iter(["hola","-60","51","-16"])
        avisos = []
        self.assertEqual(c.pedir_entero("Número",-50,50,lambda _:next(entradas),avisos.append), -16)
        self.assertEqual(len(avisos), 3)
        with self.assertRaises(ValueError):
            c.pedir_entero("Número",2,1)

    def test_fin_de_entrada_no_se_oculta(self):
        def fin(_):
            raise EOFError()
        with self.assertRaises(EOFError):
            c.pedir_entero("Número",0,1,fin)


class ConsolaU2(unittest.TestCase):
    def test_programas_reales(self):
        casos = [
            ("producto","3\n4\n","12.0"), ("bloques","","5 32"),
            ("operaciones","3\n0\n","división por cero"), ("tabla","3\n","10 30"),
            ("palabra","sol\n","sol sol"), ("pares","1\n5\n","2\n4"),
            ("triangulares","3\n","3 - 6"), ("factoriales","2\n3\n4\n","2 24"),
            ("domino","","6 6"), ("domino-n","2\n","2 2"),
            ("intervalos","0\n59\n59\n0\n0\n1\n","1 0 0"),
            ("identidad","2\n","1 0\n0 1"),
        ]
        for actividad, entrada, fragmento in casos:
            with self.subTest(actividad=actividad):
                resultado = subprocess.run([sys.executable,str(GUIA/"consola.py"),actividad],
                    input=entrada,text=True,capture_output=True,encoding="utf-8",timeout=5,
                    env={**__import__("os").environ,"PYTHONIOENCODING":"utf-8"})
                self.assertEqual(resultado.returncode, 0, resultado.stderr)
                self.assertIn(fragmento, resultado.stdout)

    def test_error_cli(self):
        resultado = subprocess.run([sys.executable,str(GUIA/"consola.py"),"factoriales"],
                                  input="-1\n",text=True,capture_output=True,timeout=5)
        self.assertEqual(resultado.returncode, 1)


if __name__ == "__main__":
    unittest.main()
