#Aqui importamos la clase tkinter q es la encargada de hacer cosa graficas
from tkinter import *

raiz=Tk()#Aqui con el metodo Tk() Es q se encarga de construir el flame o la ventana a mostras

raiz.title("Ventana De Prueba")#Aqui el metodo title() le da un titulo a nuestra ventana
#Aqui resizable() se encarga de si quieres q la ventana se pueda expandir  o abrir a lo largo y ancho
#raiz.resizable(True,False)
#Aqui iconbitmap() es el encargado de quitarle el icono q por defecto tiene python en la ventana
#raiz.iconbitmap("ico_pruebas.ico")#Aqui decimos el nombre del archivo ico q queremos q se muestre tiene q estar en la carpeta del archivo en donde esta
#geometry() se encarga de darle el tamaño q por defecto a nuestra ventana cuando inica la aplicacion
#raiz.geometry("650x350")#Aqui le pasanos el ancho y largo q queremos
#Aqui config() se encarga de darle las configuracion necesarias para nuestra ventana
raiz.config(bg="blue")

miFrame=Frame()#Aqui es para crear un frame con la clase Frame()

#Aqui se le crea una primera capa
miFrame.pack()#Se le puede pasar parametro de para q tenga una modificacion

#Aqui la clase config() se le pasamos la configuraciones necesarias para su apariencia
miFrame.config(bg="red")#Aqui le pasamos un parametro de color

miFrame.config(width="650",height="350")#Parametros de ancho y alto

miFrame.config(bd="35")#Aqui parametro de como va a ser el tamaño de un borde

miFrame.config(relief="groove")#Aqui parametro de q tipo de borde va a ser

miFrame.config(cursor="pirate")#Aqui parametro de como se va a ver el cursor cuando este en el frame posicionado

#Aqui mainloop() se encarga de mostras la ventana q se a hecho 
#este metodo siempre se va a ejecutar hazta q se cierre la ventana Asi como un ciclo
raiz.mainloop() 
#Por eso tiene q estar al final de todo