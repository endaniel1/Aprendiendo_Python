import re
#Aqui nombre
nombre1="Jara Lopez"
nombre2="Antonio Gomez"
nombre3="Maria Lopez"

#Aqui devolvera true si encuentra a Lopez
if re.search("Lopez", nombre3):
	print("Hemos Encontrado El Nombre")
else:
	print("No Hemos Encontrado El Nombre")

#Aqui cadenas de texto de lo sea
cadena1="Jara Lopez"
cadena2="56556565656"
cadena3="a56556565656"

#Aqui devolvera true si solo la cadena es de numero
if re.match("\d",cadena2):
	print("Hemos Encontrado El Numero")
else:
	print("No Hemos Encontrado El Numero")

#Aqui cualquier cosa como por ejemplo un codigo
codigo1="sdfsdfsdfsdfsdf71gfsdfsdfsdfsd"
codigo2="sdfsdfsdfsdf71hyutyhghgj"
codigo3="sdfsd sdrtvasasd asd"

#Aqui devolvera true si encuentra q el codigo tiene 71
if re.search("71", codigo3):
	print("Hemos Encontrado El Codigo")
else:
	print("No Hemos Encontrado El Codigo")