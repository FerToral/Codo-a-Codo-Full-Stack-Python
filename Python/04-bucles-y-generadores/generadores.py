def generarPares(limite):

		num=1

		miLista=[]

		while num<=limite:

			miLista.append(num*2)

			num+=1

		return miLista

print(generarPares(10))


def generarPares(limite):

		num=1



		while num<=limite:

			yield num*2

			num+=1

devuelvePares= generarPares(10)


print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))


print(next(devuelvePares))

for i in devuelvePares:
	print(i)
	
#Yield from: ayuda a simplificar el codigo de los generadores en el caso
# de utilizar bucles anidados, como los for anidados


def devuelve_ciudades(*ciudades): #El * indica que va a recibir un numero indeterminado de elementos y en forma de tupla

	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento   #Le decimos que devuelva el elemento


ciudades_devueltas= devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


def devuelve_ciudades(*ciudades): #El * indica que va a recibir un numero indeterminado de elementos y en forma de tupla

	for elemento in ciudades:
			yield from elemento    #Le decimos que devuelva el elemento desde su primer subelemento


ciudades_devueltas= devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


