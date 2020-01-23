#Aqui creo la funcion decoradorea
#Se crea como una funcion normal pero recive como parametro una funcion
def function_decoradora(function_parametro):
	#Ahora bn en esta parte se crea una funcion en el cual va a recivir dos parametros
	#Uno los argumentos de la funcion q vamos a decorar(*args)
	#Segundo si tiene clave los balores o en su defecto contante con un valor fijo a cambiar(**kwargs)
	def function_interior(*args,**kwargs):

		#Acciones adiccionales q decoran
		#Aqui en estas seccion podemos colar cualquie cosa q se quiere decorrar
		print("Vamos A Hacer Un Calculo: ")#En este caso un mesaje

		#Despues llamamos a nuestra funcion con los parametros y le asignamos los de nuestra funcion_interior
		function_parametro(*args,**kwargs)

		#Acciones adiccionales q decoran

		print("Hemos Terminado El Calculo")#En este caso un mesaje
	#Aqui sencillamente solo se retorna lo q se hizo de la funcion interna
	return function_interior

#Para decorrar una funcion solamente se coloca un @ y luego el nombre de la funcion decoradora

@function_decoradora
def suma(num1,num2,num3):
	print(num1+num2+num3)

@function_decoradora
def potencia(base,exponente):
	print(pow(base,exponente))


@function_decoradora
def resta(num1,num2):
	print(num1-num2)


#Luego sencillamente se llama a nuestra funcion normalmente como se hace

suma(7,5,8)

resta(12,10)

potencia(base=5,exponente=3)