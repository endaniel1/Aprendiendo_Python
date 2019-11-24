#Aqui importo la libreria io q sirve para abrir archivos externos
from io import open
'''
archivo_texto=open("archivo.txt","w")#Aqui open() indico el nombre del archivo
#Con w Si no esta creado lo crea y despues lo abre, sino solamente lo abre para modificarlo

frase="Estoy Estudiando Python \nDesde Hace Más De 2 Semana"#Aqui frase para Agregar

archivo_texto.write(frase)#Aqui escribo en el archivo

archivo_texto.close()#Aqui cierro el archivo
'''
'''
archivo_texto=open("archivo.txt","r")#Aqui open() indico el nombre del archivo
#Con r solamente abre un archivo q ya esta creado

texto=archivo_texto.read()#Aqui read() lo q hace es leer la informacion q esta creada

archivo_texto.close()#Aqui cierro el archivo

print(texto)#Aqui muestro el texto del archivo
'''
'''
archivo_texto=open("archivo.txt","r")#Aqui open() indico el nombre del archivo
#Con r solamente abre un archivo q ya esta creado

lineas_texto=archivo_texto.readlines()#Aqui readlines() lo q hace es leer linea por linea  y guarda en una lista

archivo_texto.close()#Aqui cierro el archivo

print(lineas_texto[0])
'''
archivo_texto=open("archivo.txt","a")#Aqui open() indico el nombre del archivo
#Con a solamente abre un archivo y le podemos agregar modificar

archivo_texto.write("\nY Es Bueno Aprender Algo Nuevo Siempre")#Aqui lo q hago es agregarle otra linea nueva al archivo

archivo_texto.close()#Aqui cierro el archivo

