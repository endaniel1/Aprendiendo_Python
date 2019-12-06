#Aqui se importa la clase para trabajar de forma grafica
from tkinter import *

raiz=Tk()#Aqui se crea la ventana

miFrame=Frame(raiz,width=1200,height=600)#Aqui se crea el Frame q va dentro la ventana
miFrame.pack()#Aqui se empaqueta para q tenga el tamaño de la ventana


miNombre=StringVar()#Aqui creamos un varible y le asignamos StringVar() q significa q la variable va a ser string
#Aqui los cuadro de texto
cuadroNombre=Entry(miFrame,textvariable=miNombre)#textvariable le asigna el valor del texto en este caso en una variable
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

#Aqui creamos un text area
#la Text() se le pasa en donde es e va estar, el ancho y lo alto
textComentarios=Text(miFrame,width=16,height=6)
textComentarios.grid(row=4,column=1,padx=10,pady=10)#Aqui le decimos el orden en donde va a estar

#Aqui creamos un scroll vertical
#Igual le decimos el contenedor padre 
#Yel comando q va hacer en este caso y q siempre va a ser es posicionarse a medida q estamos escribiendo en el texto y q se muestre en el eje y
scrollVert=Scrollbar(miFrame,command=textComentarios.yview)
#Igualmente con grid le indicamos en donde va a esta posicionado 
scrollVert.grid(row=4,column=3,sticky="nsew")#sticky le indicamos q tenga el tamoño del text area

#Aqui lo configuramos algo del text area con config()
#Q siempre posicione el scroll a medida q escribamos o q estamos escribiendo en el, con yscrollcommand
textComentarios.config(yscrollcommand=scrollVert.set)

#Aqui los label
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

#funcion q ejecuta el boton cuando lo presiona o se ejecuta
def codigoBoton():
	miNombre.set("Enrique")#Esto lo q hace es q le asigna el valor a el texto

#Aqui Button() crea un boton sencillo
#Se le pasa en donde va a esta el boton, el texto , el comando q va a ejecutar al se entre
botonEnvio=Button(raiz,text="Envio",command=codigoBoton)
botonEnvio.pack()#Aqui lo empaquetamos

raiz.mainloop()