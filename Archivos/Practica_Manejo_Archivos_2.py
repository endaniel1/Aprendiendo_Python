from io import open

archivo_texto=open("archivo.txt","r+")#Aqui open() indico el nombre del archivo
#Con r+ abre un archivo para escritura y lectura
'''
archivo_texto.seek(11)#Aqui lo q hace es posicionarse el puntero en dicha posicion para luego q lo empiece a leer

print(archivo_texto.read(11))#Si se le pasa un valor a read() lo q hace es leer solamente dicho caracteres en este caso 11

archivo_texto.seek(len(archivo_texto.read())/2)

#Aqui lo q hace es posicionar el curso a la mitad de la longitud del archivo
print(archivo_texto.read())
'''

lista_texto=archivo_texto.readlines()
lista_texto[1]="Esta Linea A Sido Modificada Desde Un Archivo Externo \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)

archivo_texto.close()

