"""def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2
def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try:
		return num1/num2

	except ZeroDivisionError:#Este error lo encontras cuando no dividis 1/0
		print("No se puede dividir por 0")
		return "Operación indeterminada"
while True:
	
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break;

	except ValueError:
		print("Operación erronea. Intentelo de nuevo")

		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
"""
#Este bloque es subceptible a tener varios fallos diferentes:
#		1. Division por 0. 2.Ingreso de caracteres
"""
def divide():
	op1= (float(input("Introduce el primer numero: ")))
	op2= (float(input("Introduce el segundo numero: ")))

	print("La division es: " + str(op1/op2))
	print("Cálculo finalizado")


divide()

#Solucion, colocamos varios Except
def divide():
	try:
		op1= (float(input("Introduce el primer numero: ")))
		op2= (float(input("Introduce el segundo numero: ")))

		print("La division es: " + str(op1/op2))
		
	except ValueError:
		print("El valor introducido es incorrecto.")
	except ZeroDivisionError:
		print("No se puede dividir por 0.")
	print("Cálculo finalizado")


divide()

#O tambien colocando solo except para que si se introduce algo fuera de lo
#	establecido inmediatamente lo tome como error.
def divide():
	try:
		op1= (float(input("Introduce el primer numero: ")))
		op2= (float(input("Introduce el segundo numero: ")))

		print("La division es: " + str(op1/op2))
		
	except:
		print("Ha ocurrido un error.")


divide()

#No es tan reconmendado porque no le indica al usuario el error

def divide():
	try:
		op1= (float(input("Introduce el primer numero: ")))
		op2= (float(input("Introduce el segundo numero: ")))

		print("La division es: " + str(op1/op2))
		
	except:

		print("Ha ocurrido un error.")

	finally:#Lo que este en este bloque se ejecutara siempre
		print("Cálculo finalizado")


divide()


def EvaluEdad(edad):

	if edad<0:#Raise nos permite incorporar nuestros propios errores
		#raise TypeError("No se permiten errores negativas")
		#Puedes cambiar la naturaleza del error. Por ejemplo:
		raise ZeroDivisionError("No se permiten edades negativas")

	if edad<28:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "cuidate"

print(EvaluEdad(-10))
"""
import math 
def calculaRaiz(num1):

	if num1<0:
		raise ValueError("El número no puede ser negativo")

	else:
		return math.sqrt(num1)

op1= (float(input("Introduce un número: ")))
try:
	print("Resultado: ",calculaRaiz(op1))
	

except ValueError as ErrorDeNumeroNegativo:#Le doy un nombre
	print(ErrorDeNumeroNegativo)

