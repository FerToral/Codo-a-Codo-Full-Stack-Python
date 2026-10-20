"""Casos representativos y recorrido de todas las consignas utilizables U1."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

GUIA=Path(__file__).resolve().parents[1]/"Python/00-guia-practica-u1/ejercicios.py"
spec=importlib.util.spec_from_file_location("u1",GUIA)
u1=importlib.util.module_from_spec(spec)
spec.loader.exec_module(u1)


class GuiaU1(unittest.TestCase):
    def test_funciones_y_bordes(self):
        self.assertEqual(u1.vocales("Abeja"),{"a":2,"e":1,"i":0,"o":0,"u":0})
        self.assertEqual(u1.divisores(-6),[1,2,3,6])
        self.assertFalse(u1.es_primo(1))
        self.assertTrue(u1.es_primo(2))
        self.assertEqual([u1.calificacion(x) for x in (0,3,5,6,7,9,10)],
                         ["Muy deficiente","Insuficiente","Suficiente","Bien","Notable","Sobresaliente","Sobresaliente"])
        self.assertEqual(u1.letra_dni(12345678),"Z")
        self.assertEqual(u1.piramide(3),["1","22","333"])
        self.assertEqual(u1.piramide(3,inversa=True),["333","22","1"])
        self.assertEqual(u1.piramide(3,acumulativa=True),["1","12","123"])
        lineas=u1.marcas_multiplos()
        self.assertEqual(len(lineas),600)
        self.assertIn("36 (Múltiplo de 4, Múltiplo de 9)",lineas)
        for accion in (lambda:u1.divisores(0),lambda:u1.calificacion(float("nan")),
                       lambda:u1.letra_dni(-1),lambda:u1.piramide(51)):
            with self.assertRaises(ValueError):
                accion()

    def test_todos_los_programas(self):
        casos={
            1:([],"Hello World"),2:([],"8"),3:(["Ana"],"Hola Ana"),
            4:(["2","3"],"5.0"),5:(["-2","-3"],"-2.0"),6:(["1","3","2"],"3.0"),
            7:(["4"],"True"),8:(["Ana"],"2"),9:(["Murcielago"],"a e i o u"),
            10:(["Ana"],"2"),11:(["Ana"],"a 2"),12:(["11"],"False"),
            13:(["30"],"2 3 5"),14:(["6"],"1 2 3 6"),15:(["6","9"],"1 3"),
            16:(["7"],"True"),17:(["18"],"No supera"),18:(["9"],"Sobresaliente"),
            20:(["uno","dos","cancelar"],"uno-dos"),21:(["2","no","3","cancelar"],"Suma: 5.0"),
            22:(["x","12345678","cancelar"],"Z"),23:([],"333"),24:(["3"],"333"),
            25:(["3"],"123"),26:([],"500"),
        }
        self.assertEqual(set(casos),set(range(1,19))|set(range(20,27)))
        for ejercicio,(datos,esperado) in casos.items():
            with self.subTest(ejercicio=ejercicio):
                entradas=iter(datos); lineas=[]
                u1.ejecutar(ejercicio,lambda _:next(entradas),lambda *args:lineas.append(" ".join(map(str,args))))
                self.assertIn(esperado,"\n".join(lineas))

    def test_eof_en_entrada_repetida(self):
        def fin(_):
            raise EOFError
        lineas=[]
        u1.ejecutar(21,fin,lambda *args:lineas.append(" ".join(map(str,args))))
        self.assertEqual(lineas,["Suma: 0"])

    def test_cli_real(self):
        proceso=subprocess.run([sys.executable,"-B",str(GUIA),"22"],input="x\n12345678\ncancelar\n",
                               text=True,capture_output=True,timeout=5)
        self.assertEqual(proceso.returncode,0,proceso.stderr)
        self.assertIn("DNI inválido",proceso.stdout)
        self.assertIn("Z",proceso.stdout)
