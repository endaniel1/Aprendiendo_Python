"""Clase de Empleado"""
class Empleado:
	#Aqui el construtos
	def __init__(self, nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	#Aqui nos devolvera siempre el texto
	def __str__(self):
		return "{} Que Trabaja Como {} Tiene Un Salario De {} $".format(self.nombre,self.cargo,self.salario)

#Aqui creamos una lista de empleados
listaempleados=[

Empleado("Juan","Director",7500),
Empleado("Ana","Presidenta",8500),
Empleado("Antonio","Administrador",2500),
Empleado("Sara","Secretario",2700),
Empleado("Mario","Botones",2100)

]
#Aqui creo un funcion q haga un calcula para un comision
def calculo_comision(empleado):
	#Aqui le agragamos la comision de los empleados a los q tenga un salario de menos de 3000 
	if empleado.salario<=3000:		
		empleado.salario=empleado.salario*1.03#Aqui la comision es de un 3%

	return empleado#Aqui retornamos a los empleados

#Aqui la funcion map() resive el nombre de la funcion, y una lista a la cual se le va a aplicar a cada iteracion  
#Aqui a diferencia de filter q map resive una funcion y no condiciones, y sirve para funcion algo mas complejas
listaEmpleadosComision=map(calculo_comision,listaempleados)
#Aqui con un ciclo retornamos los empleados y mostramos su nuevo salario con la comision
for empleado in listaEmpleadosComision:
	print(empleado)