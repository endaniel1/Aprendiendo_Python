print("Verificación de Acceso")
print("----------------------")

nota_usuario=int(input("Introducce Tú Nota, Por Favor:"))
#Aqui Mostramos un con la funcion input lo q queremos q escribas con el teclado y tranformamos eso a un valor numericon con int()

if nota_usuario < 5:
	print("Insuficiente :( :(")
elif nota_usuario < 6:
	print("Suficiente!")
elif nota_usuario < 7:
	print("Bien! :)")
elif nota_usuario < 9:
	print("Notable!! :) :)")
else:
	print("Sobresaliente!!! :D")
