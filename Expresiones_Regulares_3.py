import re
#Aqui creamos una lista de cosas para hacer
lista_nombres=[
	"Ma1",
	"Ma2",
	"MaA",
	"Se1",
	"Ba1",
	"Va1",
	"Va2",
	"Ma4",
	"Ma3",
	"MaB",
	"Ma5",
]

for elemento in lista_nombres:
	#Aqui le pasamos a findall() 
	#una condicion q el texto debe de tener  por ejemplo 
	#q TENGA Ma Y Q TRAGIA SOLO 3 Y Q TENGA DE LA A Hasta LA B
	if re.findall('Ma[0-3A-B]',elemento):
		print(elemento)#Aqui mostramos el elemento