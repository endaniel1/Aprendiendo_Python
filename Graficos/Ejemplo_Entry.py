#Aqui se importa la clase para trabajar de forma grafica
from tkinter import *

raiz=Tk()#Aqui se crea la ventana

miFrame=Frame(raiz,width=1200,height=600)#Aqui se crea el Frame q va dentro la ventana
miFrame.pack()#Aqui se empaqueta para q tenga el tamaño de la ventana

#Aqui van los caudro de textos
#grid() crea una especie de empaquetado estilo table, q se refiere q tiene columnas y filas
#Se le pasa 1er row la fila donde va estar, 2do column la columna donde va a estar, 3er y 4to Opcional para padding y cellpadding
cuadroNombre=Entry(miFrame)#Entry() lo q hace es crear un cuadro de texto, le pasamos donde es q quiera q este
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="center")#fg color del texto, justify justifica el texto al centor en este caso

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,padx=10,pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1,padx=10,pady=10)
cuadroPass.config(show="*")#show lo q hace es q el texto escrito salga de forma de *

#Aqui los label
#grid() crea una especie de empaquetado estilo table, q se refiere q tiene columnas y filas
#Se le pasa 1er row la fila donde va estar, 2do column la columna donde va a estar, 3er y 4to Opcional para padding y cellpadding
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)
#sticky alinea el texto en formato de punto cardinales, en este caso a la derecha
apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Dirección de Casa:")
direccionLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

raiz.mainloop()