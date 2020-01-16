"""def num_par(num):
	
	if num % 2==0:
		return True


numeros=[17,24,7,39,8,51,92]

print(list(filter(lambda num_par:num_par%2==0,numeros
"""
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

Empleado("Juan","Director",75000),
Empleado("Ana","Presidenta",85000),
Empleado("Antonio","Administrador",25000),
Empleado("Sara","Secretario",27000),
Empleado("Mario","Botones",21000)

]
#Aqui con la funcion filter filtramos o buscamos los empleados q tenga mas de 50000 de salario en la lista
salario_altos=filter(lambda empleados:empleados.salario>50000,listaempleados)
#Aqui lo q se hace es recorrer con un ciclo eso dichos empleados
for empleados_salarios in salario_altos:
	print(empleados_salarios)