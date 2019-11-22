
miNombreUsuario=input("Introdusca Tu Nombre de Usuario :")

#Mayuscula todas las letras
print("El Nombre de Usuario Es: ",miNombreUsuario.upper())
#Minusculas todas las letras
print("El Nombre de Usuario Es: ",miNombreUsuario.lower())
#Mayuscula la primera letra y tambien si introducimos todo el texto en mayuscula lo cambia a minuscula y la 1er letra en mayuscula
print("El Nombre de Usuario Es: ",miNombreUsuario.capitalize())
#Aqui indica la longitud del texto de donde se quiera q inicie
print("La Longitud del Nombre Desde Donde Indicamos Q Inicie: ",miNombreUsuario.count(""))
#Aqui muestro la longitud de letras q tiene despues de la busqueda segun lo q quiere, 
#los negativos es q es el ultimo numero empieza de atras y busca del indice mas bajo osea donde sea poquito
print("La longitud de Letra Q Tiene Despues De La Busqueda Es: ",miNombreUsuario.find("i"))
#Aqui devuelvo una lista expecificando de donde quiero q la separe pero sin incluir de donde quiero q la separe
print("Devuelvo Una Lista de Palabras: ",miNombreUsuario.split("e"))
#Aqui devuelve el texto sin espaciados tanto iniciales como al final
print("Borrado Los Espaciados En Blanco: ",miNombreUsuario.strip())
#Aqui replaza un texto expecificado por otro q le indiquemos
print("Replazando Espacion En Blanco Por '_': ",miNombreUsuario.replace(" ","_"))
#Aqui tranformo la primera letra de cada palabra a mayuscula
print("Transformando La Primera Letra A Mayuscula: ",miNombreUsuario.title())

edad=input("Introduce Tu Edad: ")
#isdigit devuelve True si es un valor numero y sino False
while (edad.isdigit()==False):
	print("Por Favor, Introduce un Valor Numerico: ")
	edad=input("Introduce Tu Edad: ")
if int(edad)<18:
	print("No Puedes Pasar")	
else:
	print("Puedes Pasar¡¡¡")