#Aqui se crea el generador pero con * le decimos q resiva entre uno a varias cosa valores
def devuelveCiudades(*ciudades):

	for elemento in ciudades:#aqui recorremos los valores q trae con el bucle for
		#for subElmento in elemento:#y para acceder a el subelemento lo hacemos con otro bucle for
			yield from elemento
			#Aqui con yield guardamos los elementos del generador y from lo q hace es entrar al subelemento al igual q en vez de crear otro bucle

devolver_ciudades=devuelveCiudades("Madrid", "Barcelona","España","Valencia")
#Aqui guardamos los datos del generador en una variable 

print(next(devolver_ciudades))#Aqui mostramos los datos q tiene el generador 
print(next(devolver_ciudades))#Aqui mostramos los datos q tiene el generador 