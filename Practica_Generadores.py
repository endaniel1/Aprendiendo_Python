
def generaPares(limite):#Aqui Creamos el generador

	num=1#Aqui un variable contador
	miLista=[]#Aqui un lista 

	while num<limite:#Aqui el ciclo q nos dice el limite de numero pares q se va a mostrar

		yield num*2
		#Aqui yield lo q hace es guardarnos los numeros para dentro del generador(es como una variable q guardar internamente)
		num=num+1#Aqui incrementamos 

devolverPares=generaPares(10)#Aqui creamos una varible q guarde nuestro generador
'''
for i in devolverPares:##se puede recorrer como un objeto mediante un bucle
	print(i)
'''
print(next(devolverPares))#Aqui lo q hago es muestro el primer resultado con la funcion next
print("Otras Cosas...")
print(next(devolverPares))#despues en vez de mostrar el primer resultado muestro es el q le sigue q esta almacenado con next
print("Otras Cosas...")
print(next(devolverPares))#Aqui tambien muestro es el q le sigue en la lista y asi
print("Otras Cosas...")

