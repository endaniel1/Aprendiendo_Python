salario_presidente=int(input("Introdusca el Salario del Presidente:"))
print("Salario del Presidnete "+ str(salario_presidente))
#Aqui la funcion str() tranforma una variable de tipo int a entero

salario_director=int(input("Introdusca el Salario del Director:"))
print("Salario del Presidnete "+ str(salario_director))

salario_jefe_area=int(input("Introdusca el Salario del Jefe de Área:"))
print("Salario del Presidnete "+ str(salario_jefe_area))

salario_administrativo=int(input("Introdusca el Salario Administrativo:"))
print("Salario del Presidnete "+ str(salario_administrativo))

#Aqui lo q se hace es una concadenacion de las condicciones 
#Y primero se evalua empesando de izquierda a derecha
if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
	print("Todo Es Correcto :D")
else:
	print("Algo Esta Mal Con Los Salarios")