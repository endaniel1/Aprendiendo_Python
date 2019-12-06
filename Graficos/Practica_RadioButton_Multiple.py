from tkinter import *

root=Tk()

root.title("Ejemplo Multiple Button")#un titulo sencillo para nuestra ventana

playa=IntVar()#Declara una variable tipo entera en la cual se utiliza los checkbot y radiobutton
montana=IntVar()#Declara una variable tipo entera en la cual se utiliza los checkbot y radiobutton
turismoRural=IntVar()#Declara una variable tipo entera en la cual se utiliza los checkbot y radiobutton

#funcion q muestra las opciones de viaje q hemos selecionado
def opcioneViajes():

	opcionesEscogidas=""

	#Aqui vemos si a sido selecionada una opcion para luego concanenarle un valor
	if playa.get() == 1:
		opcionesEscogidas+=" Playa"
	if montana.get() == 1:
		opcionesEscogidas+=" Montaña"
	if turismoRural.get() == 1:
		opcionesEscogidas+=" Turismo Rural"

	#Aqui lo q se hace es ponerle el texto a el Label 
	textFinal.config(text=opcionesEscogidas)

#Aqui creamos una foto para q se vea sencillamente
foto=PhotoImage(file="avion2.png")
Label(root,image=foto).pack()

#Creamos un Frame o seccion para colocar los checkbutton
frame=Frame(root)
frame.pack()

Label(frame,text="Elige Un Destino",width=50).pack()


#Aqui creamos nuestro checkbutton con Checkbutton()
#le pasamos en donde se quiere q este, el texto, una varable
#despues cuando es activado q tipo de valor tendra
#Cuando es desactivado q valor tendra
#Y q accion va a ser cuando lo selecionemos
Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcioneViajes).pack()
Checkbutton(frame,text="Montaña",variable=montana,onvalue=1,offvalue=0,command=opcioneViajes).pack()
Checkbutton(frame,text="Turismo Rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcioneViajes).pack()

#Aqui un label q muestre un texto de las opciones q hemos selecionado
textFinal=Label(root)
textFinal.pack()


root.mainloop()