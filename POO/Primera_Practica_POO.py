class Coche():#Aqui se Crea una clase plarabra reservada class
	#Aqui esta la lista de atributos o propiedades de nuestro objeto
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False
	#Fin de los atributos
	#Aqui se crea los metodos o comportamientos de nuestro objeto

	#Palabra reservada def el nombre y entre parentesis la palabra reservada self q hace referencia a los atributos del objeto osea a este 
	def arrancar(self):
		self.enMarcha=True#Accedemos con . a los atributos con la palabra reservada self
	def estado(self):
		if self.enMarcha:
			return "El Coche Esta En Marcha"
		else:
			return "El Coche Esta Parado"
	#Fin de los metodos

miCoche=Coche()#Aqui se crea una instancia de nuestro objeto coche

#Aqui se muestra los atributos o propiedades de nuestros objeto 
#para ello se utiliza la coma y luego el monbre de la variable instaciada seguidamente de un . para luego decir q tipo de propieda se quiere
print("El Largo de Chasis es:",miCoche.largoChasis)
print("El Ancho de Chasis es:",miCoche.anchoChasis)
print("El Coche Tiene",miCoche.ruedas,"ruedas")
#Aqui para acceder a un metodo sencillamente igual con un . pero en esta caso se llama como funcion
miCoche.arrancar()
print(miCoche.estado())	

print("----------------Aqui Con El Segundo Objeto------------------")
