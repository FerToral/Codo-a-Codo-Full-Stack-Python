#Concatenacion de operadores de comparacion
"""edad=7

if 0<edad<100:
	print("Edad correcta")
else:
	printf("Edad es correcta")


#Salario de personal de una empresa

salario_presidente= int(input("Introduce Salario presidente: "))

print("Salario presidente: " + str(salario_presidente))

salario_director= int(input("Introduce Director: "))

print("Salario presidente: " + str(salario_director))

salario_jefe_area= int(input("Introduce Salario Jefe de area: "))

print("Salario presidente: " + str(salario_jefe_area))

salario_administrativo= int(input("Introduce Salario Administrador: "))

print("Salario presidente: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")




#Practica de Condicionales: Operadores logicos "and", "or" 

#Programa de entrega de becas
#Quienes vivan a distnacias mayores de 40km, tenga 2 hermanos
#y que el salario de su familia sea menor o igual a 20.000

print("Programa de becas año 2020")
distancia_escuela= int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

cantidad_hermanos= int(input("Introduce el N° de hermanos: "))
print(cantidad_hermanos)

salario_familiar= int(input("Introduce el salario anual de su familia: "))
print(salario_familiar)

if distancia_escuela>40 and cantidad_hermanos>2 and salario_familiar<=20000: #Persona que cumple todas las condiciones del inicio
		print("Tienes derecho a beca")

elif distancia_escuela>40 and cantidad_hermanos>2 or salario_familiar<=20000:#Persona con el derecgo a beca por el salario de su familia, el OR tiene peso
		print("Tienes derecho a beca")
else:
		print("No tienes derecho a beca")

"""
#Programa de asignatura de materias optatias de una carrera
"""
print("Materias optativas 2020")
print("Asignatura optativas: Informática gráfica - Prueba de software - Usabilidad y accesibilidad")

asignatura= input("Escribe la asignatura escogida: ")

if asignatura in ("Informática gráfica", "Prueba de software", "Usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("Asignatura seleccionada no esta contemplada")

"""
#Para solucionar el problema de que se ponga un caracter disntio de la pañabra, se utiliza LOWER

print("Materias optativas 2020")
print("Asignatura optativas: Informática gráfica - Prueba de software - Usabilidad y accesibilidad")

opcion= input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()#Paso todo a minuscula

if asignatura in ("informática gráfica", "prueba de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("Asignatura seleccionada no esta contemplada")


