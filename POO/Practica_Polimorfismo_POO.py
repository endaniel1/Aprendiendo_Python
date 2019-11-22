"""Clase Coche"""
class Coche():	

	def desplazamiento(self):
		print("Me Desplazo Con Cuatro Ruedas")

"""Clase Moto"""
class Moto():
	def desplazamiento(self):
		print("Me Desplazo Utilizando Dos Ruedas")

"""Clase Camion"""
class Camion():
	def desplazamiento(self):
		print("Me Desplazo Utilizando Seis Ruedas")

#Aqui lo q se hace se crea una funcion q resive como parametro una variable de tipo objeto
#En la cual se utilizara para hacer lo de polimorfismo
def desplazamientoVehiculos(objeto):
	objeto.desplazamiento()
	#Aqui es donde ocurre el polimorfismo ya q en python sencillamente solo al hacer referencia al metodo q se tiene en comun entre clase se puede utilizar
	#Y En python es mas sencillo y como este tipo
	#Porque no hace falta expecificar nada solo se llama y ya

#Aqui sencillamente se puede crear cualquier objeto para luego hacer uso del polimofismo
#Ojo q esto funcionara si expecificamente y bien sea q las clases tenga el mismo metodo/comportamiento
miVehiculo=Coche()
desplazamientoVehiculos(miVehiculo)#Aqui llamamos a la funcion q hace el polimorfismo