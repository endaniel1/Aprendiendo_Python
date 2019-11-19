class Coche():#Aqui se Crea una clase plarabra reservada class


	def __init__(self):#Aqui creamos un constructor 
		#Aqui esta la lista de atributos o propiedades de nuestro objeto
		self.__largoChasis=250#Aqui con 2 __ Encapsulamos o Protegemos las variable para q siempre tenga este mismo valor fijo
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False
		#Fin de los atributos

	#Aqui se crea los metodos o comportamientos de nuestro objeto
	#Palabra reservada def el nombre y entre parentesis la palabra reservada self q hace referencia a los atributos del objeto osea a este 
	def arrancar(self,arrancamos):
		self.__enMarcha=arrancamos

		if self.__enMarcha:
			return "El Coche Esta En Marcha"
		else:
			return "El Coche Esta Parado"

	def estado(self):
		#Aqui se muestra los atributos o propiedades de nuestros objeto 
		#para ello se utiliza la coma y luego el monbre de la variable instaciada seguidamente de un . para luego decir q tipo de propieda se quiere
		print("El Coche Tiene ",self.__ruedas," ruedas. Un Ancho De ",self.__anchoChasis," Y Un Largo ",self.__largoChasis)
	#Fin de los metodos

miCoche=Coche()#Aqui se crea una instancia de nuestro objeto coche


#Aqui para acceder a un metodo sencillamente igual con un . pero en esta caso se llama como funcion
print(miCoche.arrancar(True))
miCoche.estado()	

print("----------------Aqui Con El Segundo Objeto------------------")
miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.ruedas=2#Si Aqui intentamos de cambiar el valor no se va poder 
miCoche2.estado()	
