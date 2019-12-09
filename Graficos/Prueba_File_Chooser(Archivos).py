from tkinter import *
from tkinter import filedialog
#Aqui importamos de la clase tkinter la clase filedialog q se encarga de los archivos


raiz=Tk()

#Aqui se declara una funcion en el cual se va encargar de abrir un fichero
def abreFichero():

	#Aqui creamos una varible q tenga la ruta de nuestro fichero
	#con la clase askopenfilename() de filedialog se pude manipulara archivos
	#le pasamos un titulo con titlem inciamos la ruta en la q va a iniciar por defecto q en este caso en el disco C con initialdir
	#y con filetypes le indicamos q tipo de archivos se puden selecionar en este caso se la pasa como una tupla para indicar
	fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:",filetypes=(("Todos los Ficheros","*.*"),("Fichero de Excel","*.xlsx"),
		("Fichero de Texto","*.txt")))
	print(fichero)#Aqui sencillamente se muestra la ruta del archivo

#Aqui creamos un boton q le indicamos q va a abrir un fichero y ya esta empaquetado
Button(raiz,text="Abrir Fichero",command=abreFichero).pack()


raiz.mainloop()
