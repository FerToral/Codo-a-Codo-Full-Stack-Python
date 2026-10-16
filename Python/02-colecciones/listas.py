

#listaDePersonas= ["Marcos", "Antiope", "Jerath", "Aliat"]

#print(listaDePersonas[0])

#print(listaDePersonas[-2])

#print(listaDePersonas[-3])#Contar a partir del final

#print(listaDePersonas[0:3])#Acceder a una porcion comenzando con BIT0

#print(listaDePersonas[:2])#Lo mismo de arriba

#print(listaDePersonas[2:3])#Empiezo en el BIT2, y pongo hasta el 3er elemento
						   #que concuerda con el BIT2
#print(listaDePersonas[1:4])

#listaDePersonas.append("Juliet")# Agrego Juliet a la ultima parte del Array
#listaDePersonas.insert(3,"Cort")# Meto en el BIT3 Cort

#listaDePersonas.extend(["Sol","Auriel","Dionisio"])#Pongo los 3 nombres a partir de la ultima

#print(listaDePersonas[:])

#print(listaDePersonas.index("Sol"))
#print("Sol" in listaDePersonas)
#print("Integral" in listaDePersonas)


miLista=["Martes", 5, True, 11]

miLista.extend(["Miercoles", "Jueves", "Viernes"])

miLista.remove(5)#Remuevo el valor 5
miLista.remove("Viernes")#Remuevo la palabra Viernes
miLista.pop()# Quita el ultimo elemento de la lista

print(miLista[:])
print("Pepe" in miLista) #Pregunto si Pepe esta en la lista

miLista1= ["Leche", "Galletas"]

miLista2= ["Caramelos", "Chocolates"]

miLista3= (miLista1+miLista2)*3 #Agrego ambas listas a la lista 3 y las repito 3 veces


print(miLista3)
