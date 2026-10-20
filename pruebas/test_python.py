"""Regresiones de las prácticas revisadas y ejecución de los quince scripts."""

import math
import os
from pathlib import Path
import runpy
import subprocess
import sys
import unittest


RAIZ = Path(__file__).resolve().parents[1]
PYTHON = RAIZ / "Python"


def cargar(ruta):
    return runpy.run_path(str(PYTHON / ruta))


class CondicionalesYExcepciones(unittest.TestCase):
    def test_maximo_limites_y_empate(self):
        funcion = cargar("03-condicionales/maximo.py")["devolver_maximo"]
        self.assertEqual(funcion(0, 10), 10)
        self.assertEqual(funcion(7, 7), 7)

    def test_maximo_rechaza_menor_invalido(self):
        funcion = cargar("03-condicionales/maximo.py")["devolver_maximo"]
        for notas in ((-1, 7), (7, -1), (11, 7), (7, 11)):
            with self.subTest(notas=notas), self.assertRaises(ValueError):
                funcion(*notas)

    def test_calculadora_operaciones(self):
        calcular = cargar("03-condicionales/calculadora.py")["calcular"]
        self.assertEqual(calcular(3, 2, "suma"), 5)
        self.assertEqual(calcular(3, 2, "resta"), 1)
        self.assertEqual(calcular(3, 2, "multiplica"), 6)
        self.assertEqual(calcular(3, 2, " DIVIDE "), 1.5)

    def test_calculadora_errores(self):
        calcular = cargar("03-condicionales/calculadora.py")["calcular"]
        for operandos in ((3, 0, "divide"), (3, 2, "otra"), (math.inf, 2, "suma")):
            with self.subTest(operandos=operandos), self.assertRaises(ValueError):
                calcular(*operandos)

    def test_calculadora_conserva_precision_entera(self):
        calcular = cargar("03-condicionales/calculadora.py")["calcular"]
        for entero in (9007199254740993, 10 ** 400):
            with self.subTest(entero=entero):
                self.assertEqual(calcular(entero, 0, "suma"), entero)
                self.assertEqual(calcular(entero, 2, "multiplica"), entero * 2)

    def test_media_sin_estado_global(self):
        media = cargar("03-condicionales/media_aritmetica.py")["media_aritmetica"]
        self.assertEqual(media(3, 6, 9), 6)
        self.assertEqual(media(10, 10, 10), 10)
        self.assertEqual(media(3, 3, 3), 3)

    def test_media_conserva_dominio_del_ejercicio(self):
        media = cargar("03-condicionales/media_aritmetica.py")["media_aritmetica"]
        for notas in ((0, 6, 9), (3, -1, 9), (3, 6, 11), (math.nan, 6, 9)):
            with self.subTest(notas=notas), self.assertRaises(ValueError):
                media(*notas)

    def test_raiz_cero_y_positivos(self):
        raiz = cargar("05-excepciones/raiz_cuadrada.py")["calcular_raiz"]
        self.assertEqual(raiz(0), 0)
        self.assertEqual(raiz(9), 3)

    def test_raiz_rechaza_entradas_fuera_del_dominio_real(self):
        raiz = cargar("05-excepciones/raiz_cuadrada.py")["calcular_raiz"]
        for numero in (-1, math.inf, math.nan):
            with self.subTest(numero=numero), self.assertRaises(ValueError):
                raiz(numero)


class EjecucionDeConsola(unittest.TestCase):
    def ejecutar(self, archivo, entrada):
        entorno = dict(os.environ, PYTHONIOENCODING="utf-8")
        return subprocess.run(
            [sys.executable, "-B", str(PYTHON / archivo)],
            input=entrada,
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=5,
            env=entorno,
        )

    def test_quince_practicas(self):
        casos = {
            "01-funciones/suma.py": ("", "43"),
            "02-colecciones/datos_personales.py": ("Ana\nCalle 1\n123\nAna\nCalle 1\n123\n", "Ana"),
            "02-colecciones/diccionarios.py": ("", "Buenos Aires"),
            "02-colecciones/listas.py": ("", "Martes"),
            "02-colecciones/tuplas.py": ("", "Ana"),
            "03-condicionales/asignaturas.py": ("PRUEBA DE SOFTWARE\n", "Asignatura elegida"),
            "03-condicionales/calculadora.py": ("3\n2\nsuma\n", "Resultado: 5"),
            "03-condicionales/edad_y_notas.py": ("20\n8\n", "Notable"),
            "03-condicionales/evaluacion.py": ("7\n", "Aprobado"),
            "03-condicionales/maximo.py": ("3\n7\n", "máximo es: 7"),
            "03-condicionales/media_aritmetica.py": ("3\n6\n9\n", "Media aritmética: 6.0"),
            "04-bucles-y-generadores/buscar_arroba.py": ("ana@example.test\n", "True"),
            "04-bucles-y-generadores/generadores.py": ("", "20"),
            "04-bucles-y-generadores/suma_positivos.py": ("2\n3\n0\n", "fue: 5"),
            "05-excepciones/raiz_cuadrada.py": ("9\n", "Resultado: 3.0"),
        }
        archivos = {archivo.relative_to(PYTHON).as_posix() for archivo in PYTHON.rglob("*.py")}
        # POO y U2 tienen baterías propias; el inventario sigue siendo explícito.
        adicionales = {
            "00-guia-practica-u1/ejercicios.py",
            "06-poo/Banco/banco.py", "06-poo/Banco/cliente.py",
            "07-guia-practica-u2/funciones.py", "07-guia-practica-u2/cadenas.py",
            "07-guia-practica-u2/consola.py",
            "07-guia-practica-u2/fechas.py", "07-guia-practica-u2/numeros.py",
            "07-guia-practica-u2/actividades.py",
        }
        self.assertEqual(archivos, set(casos) | adicionales)
        for archivo, (entrada, esperado) in casos.items():
            with self.subTest(archivo=archivo):
                proceso = self.ejecutar(archivo, entrada)
                self.assertEqual(proceso.returncode, 0, proceso.stderr)
                self.assertIn(esperado, proceso.stdout)

    def test_calculadora_conserva_precision_en_consola(self):
        proceso = self.ejecutar("03-condicionales/calculadora.py", "9007199254740993\n0\nsuma\n")
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        self.assertIn("Resultado: 9007199254740993", proceso.stdout)

    def test_entrada_invalida_sin_traceback(self):
        casos = (
            ("03-condicionales/maximo.py", "-1\n7\n"),
            ("03-condicionales/calculadora.py", "3\n0\ndivide\n"),
            ("03-condicionales/calculadora.py", "3.5\n"),
            ("03-condicionales/media_aritmetica.py", "tres\n"),
            ("05-excepciones/raiz_cuadrada.py", "texto\n"),
            ("05-excepciones/raiz_cuadrada.py", "-1\n"),
        )
        for archivo, entrada in casos:
            with self.subTest(archivo=archivo, entrada=entrada):
                proceso = self.ejecutar(archivo, entrada)
                self.assertEqual(proceso.returncode, 1)
                self.assertIn("Entrada inválida:", proceso.stdout)
                self.assertEqual(proceso.stderr, "")


if __name__ == "__main__":
    unittest.main()
