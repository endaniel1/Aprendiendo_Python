from tkinter import *
from tkinter import messagebox
import pymysql


#-------------------------Comienzo de Funciones--------------------
def conexionBBDD():

	try:

		miConexion=pymysql.connect("localhost","root","")
		miCursor=miConexion.cursor()
		miCursor.execute("CREATE DATABASE BBDDUsuarioPython")

		miCursor.execute('''
			CREATE TABLE BBDDUsuarioPython.DATOSUSUARIOS(
				ID INTEGER PRIMARY KEY AUTO_INCREMENT,
				NOMBRE_USUARIO VARCHAR(50),
				PASSWORD VARCHAR(50),
				APELLIDO VARCHAR(50),
				DIRECCION VARCHAR(50),
				COMENTARIOS VARCHAR(100)
			)	
		''')

		messagebox.showinfo("BBDD","BBDD Creada Con Exito")

	except:
		messagebox.showwarning("!Atención¡","La BBDD Ya Existe")
		
def salirAplicacion():
	
	valor=messagebox.askquestion("Salir","¿Desea Salir De La Aplicación?")

	if valor=="yes":
		raiz.destroy()

def limpiarCampos():

	miNombre.set("")
	miApellido.set("")
	miDireccion.set("")
	miId.set("")
	miPass.set("")
	textComentario.delete(1.0,END)#con delete le pasamos q borre del primer caracter hasta el ultimo

def crear():

	miConexion=pymysql.connect("localhost","root","","BBDDUsuarioPython")
	miCursor=miConexion.cursor()

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+miNombre.get()+
		"','"+miPass.get()+
		"','"+miApellido.get()+
		"','"+miDireccion.get()+
		"','"+textComentario.get(1.0,END)+"')")

	miConexion.commit()

	messagebox.showinfo("BBDD","Registro Insertado Con Exito!")
#-------------------------Comienzo de Variables--------------------

raiz=Tk()#Aqui la de nuestra raiz(interface)
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()
miComentario=StringVar()

#-------------------------Comienzo de Menu--------------------
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar Campos",command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#-------------------------Comienzo de Campos--------------------

miFrame1=Frame(raiz)
miFrame1.pack()

cuadroID=Entry(miFrame1,textvariable=miId)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame1,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame1,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame1,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame1,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textComentario=Text(miFrame1,width=15,height=5)
textComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame1,command=textComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")

textComentario.config(yscrollcommand=scrollVert.set)

#-------------------------Comienzo de Label--------------------
idLabel=Label(miFrame1,text="ID:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame1,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame1,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame1,text="Apellido:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame1,text="Dirección:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame1,text="Comentario:")
comentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#-------------------------Comienzo de Botones--------------------
miFrame2=Frame(raiz)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Crear",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer")
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar")
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonEliminar=Button(miFrame2,text="Eliminar")
botonEliminar.grid(row=1,column=3,sticky="e",padx=10,pady=10)




raiz.mainloop()