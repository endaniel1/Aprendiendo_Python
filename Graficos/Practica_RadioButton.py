from tkinter import *

root=Tk()

varOpcion=IntVar()#Declara una variable tipo entera en la cual se utiliza los checkbot y radiobutton

#funcion q muesta o impreme el texto en nuestra etiqueta o frame
def  imprimir():
	#print(varOpcion.get())
	#Aqui comprobamos q tipo de datos es y le asignamos a nuesta etiqueta el texto expecificado
	if varOpcion.get() == 1:
		etiqueta.config(text="Has Elegido Masculino")
	elif varOpcion.get() == 2:
		etiqueta.config(text="Has Elegido Femenino")
	else:
		etiqueta.config(text="Has Elegido Otras")


Label(root,text="Genero:").pack()

#Aqui creamos un checkbot Tipo radio con Radiobutton()
#le pasamo en donde se quiere q este, un texto, una variable para asignarle, el valor y q tipo de comando se quiere q se ejecute cuando lo presionamos
Radiobutton(root,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(root,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()
Radiobutton(root,text="Otras Opciones",variable=varOpcion,value=3,command=imprimir).pack()

#Creamos aqui un label sencillo en el cual nos va a mostrar un texto 
etiqueta=Label(root)
etiqueta.pack()


root.mainloop()