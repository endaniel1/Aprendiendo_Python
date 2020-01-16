"""Funcion lamda Sirve para poder realizar funciones sincilla osea q no tenga tanta linea de codigo"""
#lamda palabra resevada
#despues la variables
#dos puntos y lo q se va a devolver

#pow() lo q hace es devolver la potencia de un numero segun sea el expondente q le pasamos 
al_cubo=lambda numero:pow(numero,3)

#al_cubo=lambda numero:numero**3

print(al_cubo(13))#mostramos aqui el resultado de la potencia

descartar_valor=lambda comision:"¡{}! $".format(comision)

comision_Ana=15000

print(descartar_valor(comision_Ana))