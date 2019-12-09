from tkinter import *
from tkinter import messagebox
#Aqui importamos de la clase tkinter messagebox q hace para los mensajes o ventanas emegertes

raiz=Tk()#Aqui se crea la ventan

#Algunas Funciones de Ventanas Emergente
def infoAdicional():
	messagebox.showinfo("Procesador Enrique","Procesador de Texto Version: 2019")

def avisoLicencia():
	messagebox.showwarning("Licencia","Producto Bajo Licencia Windows")

def salirAplicacion():
	#valor= messagebox.askquestion("Salir","¿Desea Salir de la Aplicación?")
	valor= messagebox.askokcancel("Salir","¿Desea Salir de la Aplicación?")
	if valor == True:
		raiz.destroy()#Aqui destroy() lo q hace es q cierra la ventana principal 

def cerrarDocumento():
	valor= messagebox.askretrycancel("Reintentar","No Es Posible Cerrar. Documento Bloquead...")
	if valor == False:
		raiz.destroy()
#Fin de Algunas Funciones de Ventanas Emergente

menu=Menu(raiz)#Aqui creo el menu q este en la raiz
raiz.config(menu=menu,width=300,height=300)

#Aqui creo el primer menu  desplegable de nuestro menu
#Va a este dentro del menu y con tearoff=0 le decimos q elimine el primer sub.menu en blanco q aparece
#Despues con el add_command() añadimos  un label en el cual va a tener como texto Nuevo
#Con command le damos una funcionlida cuando le demos click
archivoMenu=Menu(menu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()#add_separator() Añade un separador para nuestro sub.menu
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)

archivoEdicion=Menu(menu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(menu,tearoff=0)

archivoAyuda=Menu(menu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)


#Aqui lo q se hace es a añadirle correspondiente lo q va a cada sun.menu
#Con add_cascade() se le pase el texto q va y despues q menu va a ser en este caso simpre va como variable
#Esto para q se haga mas facil la configuracion del mismo
menu.add_cascade(label="Archivo",menu=archivoMenu)
menu.add_cascade(label="Edición",menu=archivoEdicion)
menu.add_cascade(label="Herramientas",menu=archivoHerramientas)
menu.add_cascade(label="Ayuda",menu=archivoAyuda)

raiz.mainloop()