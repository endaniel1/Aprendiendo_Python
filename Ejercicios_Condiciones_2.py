print("Verificación de Acceso")
print("----------------------")

nota_usuario=int(input("Introducce Tú Nota, Por Favor:"))
#Aqui Mostramos un con la funcion input lo q queremos q escribas con el teclado y tranformamos eso a un valor numericon con int()

if nota_usuario < 5:#Aqui comprabamos la primero condicion
	print("Insuficiente :( :(")#Aqui mostramos el mensaje si cae en esta condicion
elif nota_usuario < 6:#Con elif hago q si no cae en la condiccion del if se vaya a esta
	print("Suficiente!")#Aqui mostramos el mensaje si cae en esta condicion
elif nota_usuario < 7:#Y si no cae en la anterior en esta o en la q le sigue
	print("Bien! :)")#Aqui mostramos el mensaje si cae en esta condicion
elif nota_usuario < 9:
	print("Notable!! :) :)")#Aqui mostramos el mensaje si cae en esta condicion
else:#Aqui si no entra en la condicciones anteriores ejecute esta
	print("Sobresaliente!!! :D")#Aqui mostramos el mensaje si cae en esta condicion
