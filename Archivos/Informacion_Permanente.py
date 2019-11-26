import pickle #Aqui importamos pickle para manejar archivos binarios

"""Clase Persona"""
class Persona:
	
	def __init__(self, nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se A Creado Una Persona Nueva Con El Nombre:",self.nombre)

	#Este Metodo lo q hace es convertir en texto la informacion de uno objeto
	#Este metodo devuelve un Json	
	def __str__(self):
		return "{} {} {}".format(self.nombre,self.genero,self.edad)
		#Aqui Aplicamos un formato q indique el nombre, el genero y edad
"""Fin Clase Persona"""

"""Clase ListaPersona"""
class ListaPersona:
	
	personas=[]#Aqui creamos una variable para guardar una lista

	def __init__(self):#Aqui tenemos el construtor
		#Aqui lo q hace es abrir un archivo de tipo binario y sino esta lo crea
		listaDePersonas=open("ficheroExterno","ab+")
		listaDePersonas.seek(0)#Aqui lo q hacemos es poner el puntero en cuando se lea el archivo al principo
		#Aqui lo q se hace es crear una excepcion por si ay un tipo de error sino se encuentra el archivo
		try:
			self.personas=pickle.load(listaDePersonas)#Aqui Cargamos en la lista con la clase load
			print("Se A Cargaron {} Personas Del Fichero Externo".format(len(self.personas)))
		except:#Aqui mandamos la excepcion 
			print("El Fichero Esta Vacio!")
		finally:#Y siempre hacemos esto al final
			listaDePersonas.close()#Cerramos el archivo abierto
			del (listaDePersonas)#Y aqui eliminamos en el uso de la memoria
		
	#Aqui metodos o comportamientos 		
	def agregarPersonas(self,p):#Metodo para Agregar personas
		self.personas.append(p)#Aqui lo q hacemos es añadir a la persona con el metodo append
		self.guardarPersonaEnFicheroExterno()#Llamamos al metodo de guardar

	def mostrarPersonas(self):#Metodo para Mostrar personas
		for p in self.personas:#Aqui sencillamente con un ciclo mostrasmos las personas q tenemos guardadas
			print(p)
	
	def guardarPersonaEnFicheroExterno(self):#Metodo para Guardar personas
		listaDePersonas=open("ficheroExterno","wb")#Aqui abrimos un archivo binario
		pickle.dump(self.personas,listaDePersonas)#Aqui con el metodo dump Añadimos la lista de persona a el archivo
		listaDePersonas.close()#Aqui cerramos el archivo
		del (listaDePersonas)#Aqui eliminamos el uso en la memoria

	def mostrarInfoFicheroExterno(self):#Metodo para Mostrar Informarcion de las personas
		print("La Informacion Del Fichero Externo Es La Siguiente:")#Aqui mensaje de lo q se va a mostrar
		for p in self.personas:#Ciclo sencillo para mostrar la informacion del fichero
			print(p)
	#Aqui Fin de los metodos o comportamientos 
"""Fin Clase ListaPersona"""

miLista=ListaPersona()
persona=Persona("Antonio","Masculino",49)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
