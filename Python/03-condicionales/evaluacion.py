# Practicas Condicionales  IF

#def evaluacion(nota):

#		valoracion="Aprobado"
#		if nota<5:
#			valoracion="Desaprobado"

#		return valoracion


#print(evaluacion(4))

#Programa de insercion de valores numericos a traves del teclado
#Error, el Input toma al valor ingresado por el teclado del tipo str


print("Programa de evaluacion de notas de alumnos: ")
#nota_alumno= input() #Podemos insentar parametros de tipo texto
nota_alumno= input("Ingrese la nota del alumno: ")
def evaluacion(nota):

		valoracion="Aprobado"
		if nota<5:
			valoracion="Desaprobado"

		return valoracion


#print(evaluacion(nota_alumno))
#para solucionar el error usaremos Int una funcion que convierte en entero el valor del teclado
print(evaluacion(int(nota_alumno)))
