milista1=["Juan",5,13,1997,13]
mitupla1=("Juan",5,13,1997)

milista=list(mitupla1)#Aqui convertimos un tupla en lista
mitupla=tuple(milista1)#Aqui convertimos un lista en tupla

#print(milista1)#Aqui mostramos la lista 
#print(mitupla1)#Aqui mostramos la tupla
#print("Juan" in mitupla)#Aqqui mostrara true si se encuentra lo q decimos sino false, tambien igual para la tupla
#print(mitupla.count(13))#Aqui mostramos cuanta cantidad de veces se encuentra el elemento, bien sea numero o string
#print(len(mitupla))#Aqui mostrar el tamoño q tiene total
print("----------------")
nombre,dia,mes,ano=mitupla1#Aqui desempaquetamos la tupla
print(nombre)#Aqui se impreme lo desempaquetado
print(dia)
print(ano)
print(mes)