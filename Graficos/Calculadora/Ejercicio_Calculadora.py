#Aqui se importa la clase para trabajar de forma grafica
from tkinter import *

raiz=Tk()#Aqui se crea la ventana

miFrame=Frame(raiz)
miFrame.pack()

operacion=""#Aqui van q tipo de Operacion fue q coloco
resultado=0#Aqui guardo los resultado finales de las Operaciones
reset_pantalla=False#Aqui para reiniciar la pantalla
acumulador_numero=0#Aqui guardos los numeros q eh puesto para hacer las Operaciones

#-------------------Pantalla---------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#03f943",justify="right")

#-------------------Pulsaciones Por Teclado---------------------------

def numeroPulsado(num):

	global operacion
	global reset_pantalla



	if reset_pantalla == True:

		numeroPantalla.set(num)
		reset_pantalla=False

	elif reset_pantalla == False:

		numeroPantalla.set(comprobarComa(numeroPantalla.get() + num))

#-------------------Funcion Suma---------------------------

def suma(num):

	global operacion
	global resultado
	global reset_pantalla

	if excepcionMenos(num,"Suma") == False:		
		return
			
	resultado+=comprobarDecimal(num)

	operacion="Suma"
	reset_pantalla=True

	round(resultado,6)
	numeroPantalla.set(resultado)

#-------------------Funcion Resta---------------------------
presiono_resta=0#Variable donde guardo las veces q presiono la tecla de resta

def resta(num):

	global operacion
	global resultado
	global acumulador_numero
	global presiono_resta
	global reset_pantalla

	if presiono_resta==0:

		if excepcionMenos(num,"Resta"):			
			return
		else:
			acumulador_numero=comprobarDecimal(num)

		resultado=acumulador_numero

	else:

		if presiono_resta==1:
			resultado=acumulador_numero-int(num)
		else:
			resultado=int(resultado)-int(num)	

		round(resultado,6)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()


	presiono_resta=presiono_resta+1
	operacion="Resta"
	reset_pantalla=True

#-------------funcion multiplicacion---------------------
presiono_multi=0

def multiplica(num):

	global operacion
	global resultado
	global acumulador_numero
	global presiono_multi
	global reset_pantalla
	
	if presiono_multi==0:

		if excepcionMenos(num,"Multiplicacion") == False and num =="":				
			return

		acumulador_numero=comprobarDecimal(num)		
		resultado=acumulador_numero

	else:

		if presiono_multi==1:			
			resultado=acumulador_numero*comprobarDecimal(num)
		else:
			resultado=resultado*comprobarDecimal(num)	

		round(resultado,6)
		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	presiono_multi=presiono_multi+1

	operacion="Multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------
presiono_divi=0

def divide(num):

	global operacion
	global resultado
	global acumulador_numero
	global presiono_divi
	global reset_pantalla
	
	if presiono_divi==0:

		if excepcionMenos(num,"Division") == False and num =="":				
			return

		acumulador_numero=comprobarDecimal(num)		
		resultado=acumulador_numero

	else:

		if presiono_divi==1:
			resultado=acumulador_numero/comprobarDecimal(num)
		else:

			resultado=comprobarDecimal(resultado)/comprobarDecimal(num)	

		numeroPantalla.set(resultado)		
		resultado=numeroPantalla.get()


	presiono_divi=presiono_divi+1
	operacion="Division"
	reset_pantalla=True

#-------------------Funcion Del Resultado---------------------------

def el_resultado():

	global resultado
	global operacion
	global presiono_resta
	global presiono_multi
	global presiono_divi

	total=0
	if operacion=="Suma":

		total=resultado+comprobarDecimal(numeroPantalla.get())
		numeroPantalla.set(round(total,6))		

	elif operacion=="Resta":

		total=comprobarTipoNumero(resultado-comprobarDecimal(numeroPantalla.get()))		
		numeroPantalla.set(round(total,6))
		presiono_resta=0

	elif operacion=="Multiplicacion":

		total=comprobarTipoNumero(resultado*comprobarDecimal(numeroPantalla.get()))
		numeroPantalla.set(round(total,6))
		presiono_multi=0

	elif operacion=="Division":

		total=comprobarTipoNumero(resultado/comprobarDecimal(numeroPantalla.get()))
		numeroPantalla.set(round(total,6))
		presiono_divi=0

	resultado=0

#-------------------Comprobar Si El Numero Es Decimal---------------------------
def comprobarDecimal(num):	

	#Aqui comparo si ay un punto para decirle a mi programa q tranforme en decimal o entero
	if '.' in num:
		return float(num)
	else:
		return int(num)

#-------------------Comprobar Si Un Numero Es Decimal---------------------------
def comprobarTipoNumero(num):	

	if float(num).is_integer():
		return int(num)
	else:
		return float(num)

#-------------------Excepcion Del Signo de Menos---------------------------
def excepcionMenos(num,tipOperacion):	

	if num == "" and tipOperacion == "Resta":
		numeroPantalla.set(numeroPantalla.get()+"-")
		return True
	else:
		return False
	


#-------------------Comprobar Si Ya Ay Una Coma---------------------------
def comprobarComa(num):	

	saberCuantasComas=0
	devolverNumero=""

	for i in range(len(num)):
	
		if num[i] != ".":

			devolverNumero=devolverNumero+num[i]

		elif num[i] ==".":

			if saberCuantasComas < 1:
				devolverNumero=devolverNumero+num[i]
				saberCuantasComas+=1
			else:
				break

	return devolverNumero
#-------------------Fila 1---------------------------

button7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
button7.grid(row=2,column=1)
button8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
button8.grid(row=2,column=2)
button9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
button9.grid(row=2,column=3)
buttonDiv=Button(miFrame,text="/",width=3,command=lambda:divide(numeroPantalla.get()))
buttonDiv.grid(row=2,column=4)

#-------------------Fila 2---------------------------

button4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
button4.grid(row=3,column=1)
button5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
button5.grid(row=3,column=2)
button6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
button6.grid(row=3,column=3)
buttonMult=Button(miFrame,text="X",width=3,command=lambda:multiplica(numeroPantalla.get()))
buttonMult.grid(row=3,column=4)

#-------------------Fila 3---------------------------

button1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
button1.grid(row=4,column=1)
button2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
button2.grid(row=4,column=2)
button3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
button3.grid(row=4,column=3)
buttonRest=Button(miFrame,text="-",width=3,command=lambda:resta(numeroPantalla.get()))
buttonRest.grid(row=4,column=4)

#-------------------Fila 4---------------------------

buttonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado("."))
buttonComa.grid(row=5,column=1)
button0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
button0.grid(row=5,column=2)
buttonSuma=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
buttonSuma.grid(row=5,column=3)
buttonIgual=Button(miFrame,text="=",width=3,command=lambda:el_resultado())
buttonIgual.grid(row=5,column=4)




raiz.mainloop()