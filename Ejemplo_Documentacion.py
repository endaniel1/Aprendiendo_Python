class Areas:
	
	"""Esta Clase Calcula La Diferentes Areas De Figuras Geometricas"""

	def areaCuadrada(lado):
		"""Aqui El calculo del area de un cuadrado
		elevado al cuadrado el lado paso por parametro"""
		return "El Area Cuadrada Es: "+str(lado*lado)

	def areaTriangulo(base,altura):
		"""Aqui el calculo del area de un triangulo, utilizando los parametros base por altura"""
		return "El Area Del Triangulo Es: "+str((base*altura)/2)

#Aqui lo q hace la clase help() es dar una ayuda de lo q hace cada cosa
#Esto lo hace indicando los comentarios q se dejan por ay para entender el funcionamiento de las cosas
help(Areas)
help(Areas.areaTriangulo)