import math#Aqui importamos la libreria math q carga las operaciones matematica un poco mas complejas

def cacularRaiz(num1):#Aqui definimos una funcion q hace la raiz cuadrada

	if num1 < 0:#Aqui vemos si el numero es menor q 0
		raise ValueError("El Numero No Posee Raiz Cuadrada")
		#Aqui lo q se hace es cambiar el valor del mensaje de la excepcion ValueError por uno en español
	else:
		return math.sqrt(num1)
		#Aqui lo q hacemos es sacar la raiz cuadra del numero con la clase sqrt q posea math

op1=int(input("Introducce Un Numero: "))#Aqui mandomos a pedir el numero

try:#Aaui hace es q si no ay algun tipo de eerror ejecute este y siga con el programa
	print(cacularRaiz(op1))#Mostramos Aqui la raiz cudrada	
	#Aqui vemos q tipo de excepcion se tiene y con as se le asigna un nombre q se pueda entender mejor y en español
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)#Aqui mostramos el mensaje q carga ErrorDeNumeroNegativo q le asigamos con raise

#Aqui mostramo otro msj suponiendo q queremos colocarle mas lineas de codigo a nuestro programo
print("Programa todavia en Ejecucion")