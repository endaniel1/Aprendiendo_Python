midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}#Aqui variable diccionario
midiccionario["Italia"]="Lisboa"#Aqui Asignamos el valor de una clave 

print(midiccionario)#aqui mostramos el cambio q se hizo

midiccionario["Italia"]="Roma"#Aqui volvemos a cambiarle el valor

print(midiccionario)#Aqui mostramos q se cambio correctamente el valor

del midiccionario["Reino Unido"]#Aqui eleiminamos una clave de un diccionario

print(midiccionario)#Aqui mostramos q se elimino correctamente

print("----------------")

midiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteo":232}#Aqui creamos otro diccionario q tiene claves y/o valores numericos 

print(midiccionario2)#Aqui mostramos el diccionario

print("----------------")

mitupla=["España","Francia","Reino Unido","Alemania"]#Aqui creamos un tupla nueva
midiccionario3={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
#Aqui creamos un diccionario apartir de la tupla respectivos nombres 

print(midiccionario3)#Aqui mostramos el diccionario
print(midiccionario3["Francia"])#Aqui mostramos el valor de la clave del diccionario

print("----------------")

midiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993]}}
#Aqui creamos un diccionario q tiene un diccionario interno y ademas una tupla agregada

print(midiccionario4.keys())#Aqui mostramos los nombres de todas las claves del diccionario
print(midiccionario4.values())#Aqui mostramos los valores q tiene cada clave del diccionario
print(len(midiccionario4))#Aqui mostramos la longitud q tiene el diccionario
print(midiccionario4)#Aqui mostramos el diccionario completo