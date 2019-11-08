print("Programa de Evalucion de Nota de Alummno")
print("----------------")

nota_alumno=input("Introduce la Nota del Alumno")
#Aqui aguardamos lo q escribe por tecaldo con la funcion input(), Dentro le colocamos el texto q tenemos q ver

def evalucion(nota):#Aqui una funcion
	valoracion="Aprobado"
	if nota < 5:#Aqui compramos la nota q le pasamos en este caso 5
		valoracion="Reprobado"#Aqui cambiamos el valor de la varible suspenso
	return valoracion#aqui retornamos el valor de la varible suspenso

print(evalucion(int(nota_alumno)))
#Aqui mostramos el resultado devuelto de la funcion y tranformamos o decimos q el valor es entero con la funcion int()
