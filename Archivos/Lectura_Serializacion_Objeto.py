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

ficheroApertura=open("losCoches","rb")#Aqui abrimos un archivo binario para solo lectura con rb
#Aqui cargamos el fichero con la clase load() de pickle
misChoches=pickle.load(ficheroApertura)

ficheroApertura.close()#Aqui cerramos el archivo q utilizamos

del (ficheroApertura)#Aqui eliminamos el archivo en el uso de la memoria

#Aqui con un ciclo sencillo recorremos la lista sencilla donde estan los coches
for x in misChoches:
	print(x.estado())