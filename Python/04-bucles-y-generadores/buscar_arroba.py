"""for i in [1,2,3]:
	print(i)

for i in ["Primavera","Otoño","Inviermo","Verano"]:
	print(i)

for i in  ["Fernando", "Toralez", 19]:
	print("Hola", end=" . ") #pONE EN UNA MISMA el mensaje


for i in "fernando": #repito la cantidad de caracteres de la palabra
	print("Hola", end=" . ") #pONE EN UNA MISMA el mensaje
	

email=False
miEmail= input("Ingrese su dirección de mail:")

for i in miEmail: #repito la cantidad de caracteres de la palabra
	
	if i == "@":
		email=True

if email==True:
	print("El mail es correcto")
else:
	print("El mail es incorrecto")"""
	
"""for i in range(9):
	print(i, end=" ")

for i in range(5,50,3): #Voy del 5-50 de tres en tres 5,8,11...47
	print(f"Valor de la variable {i}")#la f permie meter el valor de i en el string

valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):
	
	if email[i]=="@":
		valido=True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")

i=1
while i<=10:
	print("Ejecucion " + str(i))
	i+=1
print("Termino la ejecucion")

edad= int(input("Introdusca tu edad: "))

while 0>edad or edad>100:
	print("Has introducido una edad incorrecta. Vueklve a intertarlo")
	edad= int(input("Introdusca tu edad: "))
print("Gracias por colaborar")
print("Edad del aspirante: " + str(edad))"""

"""
import math
print("Programa de calcula raiz cuadrada: ")

numero= int(input("Introdusca un numero: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Han consumido demasiados intentos. El programa ha finalizado")
		break; #Sale del buclle while
	numero = int(input("Introdusca un numero: "))
	if numero<0:
		intentos+=1

if intentos<2:
	solucion= math.sqrt(numero)
	print("La raiz cuadrada de" + str(numero) + " es " + str(solucion))

if intentos==2:
	
	print("Ha sobrepasado el numero de intentos posibles, reinicie el programa")
"""
#Clase 7 Bucles. Continue, pass, else
"""
for letra in "Python":
	if letra== "h":
		continue
	print("Viendo la letra: " + letra)

nombre= "Fernando Toralez"
contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1

print(contador)


while True:
	pass #devuelve un null
	#mantiene al programa ocupado hasta que se rompa el programa

class Miclase:
	pass #para implementar mas tarde
		#Hace como si esta clase no existiese y es como dejar
		# el trabajo para mas tarde
"""
email= input("Ingrese direccion de mail: ")

for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False

print(arroba)
