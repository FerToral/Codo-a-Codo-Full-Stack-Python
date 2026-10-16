# Practicas Condicionales  IF y ELSE

edad_usuario= int(input("Introduce tu edad: "))

if edad_usuario<18:
	print("No pasar")

elif edad_usuario>100:
	print("La edad es incorrecta")

else:
	print("Puedes pasar")

#Los Elif son lo mismo que en C de los else if(parametros)
nota_alumno= int(input("Introduce la nota del alumno: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")

