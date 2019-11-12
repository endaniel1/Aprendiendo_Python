'''
edad=int(input("Introduce Tu Edad: "))#Aqui lo q se hace es pedir la edad

#Aqui evaluamos si la edad es menor q 0 y mayor a 100
#si es asi cae en el ciclo
while edad < 0 or edad > 100:

	print("Has Introducido una Edad Negativa. Vuelve a Intentarlo")#Mostramos un mensaje de error

	edad=int(input("Introduce Tu Edad: "))#Y volvemos a pedir aqui la edad
print("Gracias Por Colaborar. Puedes Pasar.")
print("Edad del Aspirante "+ str(edad))

'''
import math#Aqui se hace es importar la libreria math
print("Programa Para El Calculo De La Raiz Cuadra")#Mostramos un mensaje
print("----------------")
numero=int(input("Introduce Un Numero: "))#Aqui pedimos q introdusca un numero

intentos=0#Creamos un variable q tenga los intentos del usuario

while numero < 0:
	print("No Se Puede Hayar Y Hacer La Raiz De Un Numero Negativo")#Mostramos un mensaje de erro

	if (intentos==2):#Aqui vemos cuantos intento tiene el usuario
		print("Haz Consumido El Numero De Intento. El Programa A Finalizado¡")#Mostramos un mensaje
		break;#Aqui break lo q hace es salir del flujo del ciclo q estas

	numero=int(input("Introduce Un Numero: "))#Aqui volvemos a pedir q introdusca el numero
	if numero < 0:#Evaluamos aqui si el numero q introdujo es negativo
		intentos=intentos+1#Aqui Incrementamos los intentos

if intentos < 2:#Vemos aqui si intentos todavia es menor 2 para hacer el calculo

	#Aqui realizamos el calculo llamando a el metodo sqrt de la clase math q es el q hace el calculo de la raiz cuadrad
	solucion=math.sqrt(numero)
	print("La Raiz Cuadra de "+str(numero)+" Es "+str(solucion))#Aqui mostramos el mensaje de la raiz cuadrada del numero