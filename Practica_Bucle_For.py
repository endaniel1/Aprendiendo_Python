'''
contador=0

miEmail=input("Introducce Tu Direccion de email: ")

for i in miEmail:
	
	if (i=="@" or i=="."):
		contador=contador+1
	

if contador==2:
	print("Email Es Correcto!!!")
else:
	print("El Email No Es Correcto")

#este codigo no es del todo correcto en realida es solo pra ver q el buble tambien recorre string
'''
'''
for i in range(5,50,3):
	print(f"El Valor de la Variable es: {i}")
'''
valido=False

email=input("Introducce Tu Direccion de email: ")

for i in range(len(email)):
	
	if email[i]=="@":
		valido=True
	

if valido:
	print("Email Es Correcto!!!")
else:
	print("El Email No Es Correcto")
