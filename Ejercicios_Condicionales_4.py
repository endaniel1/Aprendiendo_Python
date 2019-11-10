'''print("Programa de Becas Año 2019")
print("----------------")

distancia_escuela=int(input("Introduce La Distancia A La Escuela en Km: "))
print(distancia_escuela)

numeros_hermanos=int(input("Introduce El N° De Hermanos: "))
print(numeros_hermanos)

salario_familiar=int(input("Introduce El Salario Anual Bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numeros_hermanos > 2 or salario_familiar <= 20000:
	print("Tiene Derecho A Beca ")
else:
	print("No Tiene Derecho A Beca ")
'''

print("Asignaturas Optativa Del 2019")
print("Asignaturas Optativa: 'Informatica Grafica' - 'Prueba de Software' - 'Usabilidad y Accesibilidad'")
opcion=input("Introduce La Asignatura a Escoger: ")

asignatura=opcion.title()#Aqui la funcion titlt() traforma cada primera palabra de un string a mayuscula
#existe mas como tower(), upper(), serializable() ect.

#Aqui evaluo una varible a ver si tiene los valores correspendiente
#in() devolvera true si coincide con algunas de las opciones
if asignatura in("Informatica Grafica","Prueba de Software","Usabilidad y Accesibilidad"):
	print("Asignatura Elegida "+ asignatura)
else:
	print("La Signatura Escogida No Esta o No Esta Completada")
