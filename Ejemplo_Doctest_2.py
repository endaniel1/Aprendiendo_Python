import math

def raizCuadrada(listaNumeros):
	# Aqui lo nuevo es q con los tres ...
	# Lo q se hace es para cuando se quiera concadenar en este caso porque python respeta el ordenamiento de codigo
	# Para poder ejecutar lo q a continuacion va a hacer es para ello q se utilizan
	# Despues tenemos aqui para q ejecute algun tipo de error copiamos primero la clausura q manda o señala
	# Y el tipo de error, sincillamente lo q se hace es eliminar la parte internerna q se tiene y agregarle ...
	# Para q pueda ejecutar la prueba correctamente
	# Ojo esta prueba funcion si se espera ese tipo de errores porque sino, nos dira q eso esta mal
	"""
	La Funcion Devuelve Una Lista Con La
	Raiz Cuadrada De Los Elementos Numericos
	Pasandos Por Parametros En Otras Lista

	>>> lista=[]
	>>> for i in [4,-9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4,-9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
  		...
	ValueError: math domain error
	"""
	#Aqui math.sqrt(n) lo q hace para el ciclo es hacer una raiz cuadra de los numero q se siente en la lista
	#Aqui retornamos esto valores en un lista nueva
	return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9,16,25,36]))

import doctest
doctest.testmod()