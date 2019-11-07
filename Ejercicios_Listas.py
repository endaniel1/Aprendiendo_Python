miLista=["Maria","Pepe","Marta",True,7.5]
miLista2=["Julian","Pedro"] * 3#Aqui se crea una nueva lista y se multiplica 3 veces o mkejor dicho se repite 3 veces concadenada


#miLista.append("Sandra")#Aqui para agregar al final de un lista
#miLista.insert(2,"Sandra")#Aqui para insertar un elemento en el indice q le indique
miLista.extend(["Sandra","Ana",5])#Aqui para agragar al final de un lista otra lista

print(miLista[:])
print(miLista.index("Maria"))#Aqui para buscar el indice del elemento a buscar 
#pero solo nos devolvera el indice del elemento q encuentre primero por order si ay repetido
print("Pepess" in miLista)#Aqui comparo si existe un elemento de la lista y devuelve true si existe y false si no

print("----------------")

#miLista.remove(5)#Aqui eliminamos el elemento q queromos indicandole bien sea el numero, el texto, el float o el booleano
miLista.pop()#Aqui lo q hacemos es eliminar el ultimo elemento de la lista
print(miLista[:])

print("----------------")

miLista3=miLista+miLista2#Aqui lo q hacemos es sumar la dos lista con el opedor suma como si estuvieramos concanedandola
print(miLista3)


