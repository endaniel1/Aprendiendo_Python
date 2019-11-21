"""Clase persona"""
class Persona():

	def __init__(self,nombre,edad,lugar_residencia):#Aqui el Contrutor
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	#Aqui el metodos o comportamientos
	def descripcion(self):
		print(" Nombre:",self.nombre,"\n Edad:",self.edad,
			"\n Lugar de Residencia:",self.lugar_residencia)

""" Clase Empleados"""
class Empleados(Persona):
	#Aqui constructor 
	def __init__(self, salario,antigûedad,nombre_empleado,edad_empleado,residencia_empleado):
		#Aqui el metodo super llama al contrutor de la clase padre para q tenga sus caracteristicas
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
		self.salario=salario
		self.antigûedad=antigûedad

	#Aqui el metodos o comportamientos
	#Aqui Sustituyo el metodo descripcion de la clase padre o algo asi creo es ese el termino
	def descripcion(self):
		super().descripcion()#Aqui llamo al metdo descripcion de la clase padre con el metodo super
		print(" Salario",self.salario,"\n Antigûedad",self.antigûedad)#Aqui muestro mensaje

Manuel=Persona("Manuel",50,"España")

Manuel.descripcion()#Aqui llamo al metedo descripcion de Persona

#Aqui muestro si es verdad q nuestro objeto Mauel pertenece a la clase Empleados
#Si es verda nos devolvera True Sino False
print(isinstance(Manuel,Empleados))

Antonio=Empleados(12000,10,"Antonio",55,"España")
Antonio.descripcion()
print(isinstance(Antonio,Empleados))
		
		
	
	