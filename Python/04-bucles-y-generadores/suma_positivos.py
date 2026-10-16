"""print("Programa Ejercicio 1")

numeros= int(input("Ingrese los valores numericos: "))

mayor= numeros

while numeros>= mayor:
	if numeros>=mayor:
		mayor= numeros
		numeros= int(input("Ingrese los valores numericos: "))
	if numeros<mayor:
		print("Se ha ingresado un numero menor al anterior. El programa Finalizara")
		break;

print("Ha finalizado el prograna. El numero mayor ingresado fue: " + str(mayor) )

"""

print("Programa Ejercicio 2")

numeros= int(input("Ingrese los valores numericos: "))
suma=0


while numeros>0:
	if numeros>0:
		suma+=numeros
		numeros= int(input("Ingrese los valores numericos: "))

	
print("Ha finalizado el prograna. La suma de los numeros positivos ingresados fue: " + str(suma) )
