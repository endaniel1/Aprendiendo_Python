print("Programa de Ejecucion de Excepciones")
print("'Calculadora Sencilla'")
print("----------------")
print("----------------")
def suma(num1,num2):#Aqui la funcion de suma
	return num1+num2#Aqui Retornamos la suma de los numero

def resta(num1,num2):#Aqui la funcion de resta
	return num1-num2#Aqui Retornamos la resta de los numero

def multiplica(num1,num2):#Aqui la funcion de multiplicacion
	return num1*num2#Aqui Retornamos la multiplicacion de los numero

def divide(num1,num2):#Aqui la funcion de divicion
	try:#Aqui lo q hacemos es q sino cae apartie de aqui e la respectiva excepcion hace esto
		return num1/num2#Aqui retornamos si no tiene excepcion
	except ZeroDivisionError:
	#Aqui ZeroDivisionError es la excepcion de q no se puede dividir ningun numero en 0 y si cae hace lo siguiente
		print("No Se Puede Dividir Entre 0")#Aqui mostramos un mensaje 
		return "Operacion Erronea"#Aqui retornamos otro mensaje
		
while True:#aaqui lo q hago es q siempre q se verdadero me ejecute esto
	try:#mando una q si no ay un excepcion vaya ejecuntado esto
		op1=int(input("Introduce El Primer Numero: "))#Aqui pedimos el primer numero

		op2=int(input("Introduce El Segundo Numero: "))#Aqui pedimos el segundo numero
		break#Cuando finalizo q todo este bn rompo el ciclo con break
	except ValueError:
	#Aqui ValueError es la excepcion de tipo de datos expecificado en este caso q se numerico y si cae hace lo siguiente
		print("Introdusca Solo Numero Para Poder Continuar!!!")#AQUI UN MENSAJE Q SE LE INDICA Q SOLO PUDE SER NUMERO
	
#Aqui le decimos a el usuario q tipo de operacion desea realizar
operacion=input("Introducce la Operacion a Realizar(suma,resta,multiplica,divide): ")

if operacion =="suma":#Aqui probamos si es suma
	print("La Suma De los Numero Es: "+str(suma(op1,op2)))

elif operacion =="resta":#Aqui probamos si es resta
	print("La Resta De Los Numero Es: "+str(resta(op1,op2)))
	
elif operacion =="multiplica":#Aqui probamos si es multiplicacion
	print("La Multiplicacion De Los Numero Es: "+str(multiplica(op1,op2)))
	
elif operacion =="divide":#Aqui probamos si es divicion
	print("La Divicion De Los Numero Es: "+str(divide(op1,op2)))

else:#Aqui sino es ninguna de las anterior
	print("Operacion No Completada")

print("Operacion Termina. Aqui Continuacion De La Ejecucion Del Programa....")
#AQUI BUENOS DIGAMOS Q AY MAS LINEAS DE CODIGO Q QUEREMOS Q SE EJECUTEN DESPUES DE LO ANTERIOR
