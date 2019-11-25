#Aqui importamos la clase pickle q es la q nos hace para la serializacion 
import pickle

"""Clase Vehiculos"""
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

''' Aqui Creamos Los Objetos Vehiculos A Almacenar  '''
coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Seat","Leon")
coche3=Vehiculos("Renault","Megane")

coches=[coche1,coche2,coche3]#Aqui creamos una lista sencilla donde almacenamos lo objetos coches
#Aqui abrimos un archivo con open()
fichero=open("losCoches","wb")#Si existe el archivo lo abre sino lo crea con "wb"
#Aqui dump() lo q hace es un volcado de archivo y en este caso le añadimos la lista de nombre a el archivo o fichero
pickle.dump(coches,fichero)

fichero.close()#Aqui cerramos el archivo q utilizamos

del (fichero)#Aqui eliminamos el archivo en el uso de la memoria

