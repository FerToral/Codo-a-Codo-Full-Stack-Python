
primer_numero= int(input("Ingresar primer numero: "))
segundo_numero= int(input("Ingresar segundo numero: "))

def DevuelveMax(nota1, nota2):
	if nota1<nota2:
		mayor=nota2
	elif nota1>nota2:
		mayor=nota1
	else:
		mayor=nota1
	return mayor

if DevuelveMax(primer_numero,segundo_numero)>10:
	print("Error al insertar alguno de las notas")
elif DevuelveMax(primer_numero,segundo_numero)<0:
	print("Error al insertar alguno de las notas")
else:
	print("El valor maximo es: ",DevuelveMax(primer_numero,segundo_numero))

	
