
n1= float(input("Ingresar Primer Numero: "))
n2= float(input("Ingresar Segundo Numero: "))
n3= float(input("Ingresar Tercer Numero: "))
c=0

def MediaAritmetica(Nota1, Nota2, Nota3):
	if Nota1<=0 or Nota2<=0 or Nota3<=0:
		return "Error"
	elif Nota1>10 or Nota2>10 or Nota3>10:
		return "Error"
	else:
		media= (Nota1+ Nota2+ Nota3)/3
		return media

print(MediaAritmetica(n1,n2,n3))



posicion= ["Imgresar Primer Numero: ", "Ingresar Segundo Numero: ", "Ingresar Tercer Numero: "]
n= [n1, n2, n3]
c=0

for i in range(3):
	n[i]=float(input(posicion[i]))
	c+=1

def MediaAritmetica(Nota1, Nota2, Nota3):
	if Nota1<=0 or Nota2<=0 or Nota3<=0:
		return "Error"
	elif Nota1>10 or Nota2>10 or Nota3>10:
		return "Error"
	else:
		media= (Nota1+ Nota2+ Nota3)/c
		return media

print(MediaAritmetica(n[0],n[1],n[2]))


posicion= ["Primer", "Segundo", "Tercer"]
n= [n1, n2, n3]
c=0

for i in range(3):
	n[i]=float(input("Ingresar "+posicion[i]+" Numero: "))
	c+=1

def MediaAritmetica(Nota1, Nota2, Nota3):
	if Nota1<=0 or Nota2<=0 or Nota3<=0:
		return "Error"
	elif Nota1>10 or Nota2>10 or Nota3>10:
		return "Error"
	else:
		media= (Nota1+ Nota2+ Nota3)/c
		return media

print(MediaAritmetica(n[0],n[1],n[2]))

