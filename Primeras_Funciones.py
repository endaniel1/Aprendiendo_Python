def mensaje():#declacion de la funcion de un mensaje sencillo

	#Cuerpo de la funcion
	print("Estoy aprendiendo python")
	print("Estoy aprendiendo intrucciones basica")
	print("Poco a poco ire avanzando")
	#fin de cuerpo de la funcion

mensaje()#Aqui la llamada de la funcion

mensaje()#Aqui la llamada de la funcion

mensaje()#Aqui la llamada de la funcion

print("----------------")

def suma3():#Aqui la llamada de la funcion de una suma de dos numero
	num1=5
	num2=2
	print(num1+num2)

suma3()#Aqui la llamada de la funcion de suma
suma3()
suma3()#Aqui la llamada de la funcion de suma

print("----------------")

def suma1(num1,num2):#Aqui la llamada de la funcion de una suma de dos numero sin retorno
	
	print(num1+num2)#y mostramos su resultado aqui

suma1(5,7)#Aqui la llamada de la funcion de suma

suma1(2,3)#Aqui la llamada de la funcion de suma

suma1(35,35)#Aqui la llamada de la funcion de suma

print("----------------")

def suma2(num1,num2):#Aqui la llamada de la funcion de una suma de dos numero con retorno
	
	resultado=num1+num2

	return resultado#y retornamos su resultado aqui

almacenar_resultado=suma2(7,5)#Aqui almacenamos en una variable y hacemos la llamada
print(almacenar_resultado)#y mostramos aqui el resultado de la variable
