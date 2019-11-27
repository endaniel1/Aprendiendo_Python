from tkinter import *#Aqui importamos la clase q se encarga de lo de interfaz grafica

root=Tk()#Aqui la clase Tk() q hace lo de la ventana

#Aqui se crea un Frame
#Se le pasa la varible de donde se va a agregar, ademas en este caso un ancho y un largo q va tener por defecto
miFrame=Frame(root,width=500,height=400)#Esto puede tener mas cosa para agregarle

miFrame.pack()#Aqui pack() se encarga de empaquetar eso

#Aqui agregamos un Label con la clase Label()
#Y le pasamos en donde va esta agregado, un texto, como van las letras(color)
#Una fuente con su tamaño, Ademas le agragamos la clase place()
#Q es la q se encarga de darle la posicion en donde va a estar en el eje x,y correspondiente a Frame en donde esta
Label(miFrame,text="Este es un Label",fg="red",font=("Comic Sans MS",18)).place(x=200,y=100)

root.mainloop()#Aqui lo de la la clase mainloop() q hace lo de mostrar las cosas