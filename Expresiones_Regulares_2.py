import re
#Aqui creamos una lista de cosas para hacer
lista_nombres=[
	"Hombres",
	"Mujeres",
	"Mascotas",
	"Niños",
	"Niñas"	
]
#Aqui con un ciclo recorremos la lista
for elemento in lista_nombres:
	#con la clase findall() buscamos todos lo elemento q tenga dicha coincidencia
	if re.findall('Niñ[oa]s',elemento):
		print(elemento)#Aqui mostramos el elemento
	