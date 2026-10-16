# Diccionarios

miDiccionario= {"Argentina":"Buenos Aires", "Alemani":"Berlin", "Francia":"Paris"}

print(miDiccionario["Argentina"])
print(miDiccionario)

#Agregar nuevos elementso y claves al diccionario

miDiccionario2= {"Argentina":"Buenos Aires", "Aleman":"Berlin", "Francia":"Paris"}

miDiccionario2["Italia"]= "Lisboa" #Agregamos los elemntos
print(miDiccionario2)

miDiccionario2["Italia"]= "Roma"  #Sobrescrbimos el valor en la clave Italia
print(miDiccionario2)

del miDiccionario2["Francia"]	  #Eliminamos un elemento con su clave
print(miDiccionario2)

# Usar una Tupla´para asignar una cantidad de valores
miTupla= ["Argentina", "Brasil", "Paraguay", "Uruguay"] #Cargo mi Tupla
miDiccionario3= {miTupla[0]: "Buenos Aires", miTupla[1]:"Brasilia", miTupla[2]: "Asuncion", }
#Posiciono los valores de la Tupla con las Claves correspondientes
print(miDiccionario3)

print(miDiccionario3["Brasil"])

# Diccionario que almacene en su interior junto a otros valores y na Tupla de valores

miDiccionario4= {19:"Edad", "Nombre":"Fernando Toralez", "Profesion":"Tecnico Electronico", "Certificados": [2017,2018,2019]}
print(miDiccionario4["Certificados"])

#Diccionario con una tupla adentro
miDiccionario5= {19:"Edad", "Nombre":"Fernando Toralez", "Profesion":"Tecnico Electronico", "Certificados":{"Años":[2017,2018,2019]}}

print(miDiccionario5["Certificados"]) #Muestro el valor de la clave Certifocados
print(miDiccionario5)
print(miDiccionario5.keys())		#Muestro las Clave
print(miDiccionario5.values())		#Muestro los Valores
print(len(miDiccionario5))			#Cantidad de elementos de miDiccionario
