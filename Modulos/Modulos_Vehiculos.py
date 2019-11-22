"""Super Clase Vehiculos"""
class Vehiculos(object):	
	def __init__(self, marca, modelo):#Aqui el Construtor
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelerar=False
		self.frenar=False

	#Aqui los metodos o comportamiento
	def arrancar(self):
		self.arrancar=True
	def acelerar(self):
		self.acelerar=True
	def frenar(self):
		self.frenar=True
	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn Marcha:",
			self.enMarcha,"\nAcelerando:",self.acelerar,"\nFrenando:",self.frenar)
	#Aqui Fin los metodos o comportamiento

#Aqui la clase Furgoneta
class Furgoneta(Vehiculos):#Dentro del pararentesis hereda de la clase vehiculos
	#Aqui los metodos o comportamiento
	def carga(self,carga):
		self.cargando=carga
		if self.cargando:
			return "La Furgoneta Esta Cargada"
		else:
			return "La Furgoneta No Esta Cargada"
	#Aqui Fin los metodos o comportamiento
#Aqui Fin de clase Furgoneta

#Aqui la clase Moto
class Moto(Vehiculos):

	hCaballito=""#Aqui un atributo o caracteristica
	#Aqui los metodos o comportamiento
	def caballito(self):
		self.hCaballito="Voy Haciendo Caballito"

	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn Marcha:",
			self.enMarcha,"\nAcelerando:",self.acelerar,"\nFrenando:",self.frenar,"\n",self.hCaballito)
	#Aqui Fin los metodos o comportamiento
#Aqui Fin de la clase Moto

#Aqui la clase Vehiculos Electricos
class VElectricos(Vehiculos):	

	def __init__(self,marca,modelo):#Aqui el construtor

		super().__init__(marca,modelo)#Aqui con el metodo super lo q hago es llamar al construtor de la clase padre y le paso los valores
		self.autonomia=100
	#Aqui los metodos o comportamiento
	def cargarEnergia(self):
		self.cargando=True
	#Aqui Fin los metodos o comportamiento
#Aqui Fin de la clase Vehiculos Electricos
