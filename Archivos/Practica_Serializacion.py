#Aqui importamos la clase pickle q es la q nos hace para la serializacion 
import pickle
'''
listas_nombres=["Pedro","Ana","Isable","Maria"]#Aqui creamos una lista sencilla
#Aqui abrimos un archivo con open()
fichero_binario=open("listas_nombres","wb")#Si existe el archivo lo abre sino lo crea con "wb"
#Aqui dump() lo q hace es un volcado de archivo y en este caso le añadimos la lista de nombre a el archivo o fichero
pickle.dump(listas_nombres,fichero_binario)

fichero_binario.close()#Aqui cerramos el archivo q utilizamos

del (fichero_binario)#Aqui por si acaso eliminamos la informacion en memoria
'''

fichero=open("listas_nombres","rb")#Aqui abrimos un archivo binario para solo lectura con rb
#Aqui cargamos el fichero con la clase load() de pickle
lista=pickle.load(fichero)

print(lista)#Y una vez listo lo q hacemos es mostras eso datos

fichero.close()#Aqui cerramos el archivo q utilizamos