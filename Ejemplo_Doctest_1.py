def  compruebaEmail(emailUsuario):

	#Aqui sencillamente vamos a hacer las pruebas en nuestras lineas de comentarios
	#los tres >>> represenata asi la linea de prueba a ejecutar 
	#lo q se hace es sencillo solamente se llama a la funcion compruebaEmail() y se le pasa un string con un email para q lo compruebe
	#Despues sencillamente se va aevaluar con las condiciones correspondiente
	#Y se pasa no devolvera nada pero sino devolvera y e indicara lo q esta mal
	"""
	La Funcion Comprueba el Email
	Recibo En Busca de Un @. Si Tiene Un @
	Es Correcto, Si tiene Mas De Un @ Es Incorrecto
	Si El @ Esta Al Final Es Incorrecto 	
	
	
	>>> compruebaEmail("juan@cursos.es")
	True

	>>> compruebaEmail("juan@cursos.es@")
	False

	>>> compruebaEmail("juancursos.es")
	False

	>>> compruebaEmail("juan@cursos@.es")
	False
	"""
	#Aqui sencillamente se cuenta cuantas veces esta el @ 
	arroba=emailUsuario.count("@")
	#Aqui comprobamos si ay @ mas de 1
	#O si el ultimo digito de nuestra string tiene @
	#O sino ay el @
	if (arroba!=0 or emailUsuario.rfind("@")==(len(emailUsuario)-1) or emailUsuario.find("@")==0):
		return False
	else:
		return True

#Aqui importamos el modulo de doctest 
#En el cual nos va a hacer la prubas para ver si esta bn nuestro trabajo
import doctest
doctest.testmod()
#la clase testmod() buscare q linea de comentario estar para ejecutarce la prueba 
#Ojo esto no resultara muy si hay algo q se muestre porque se interumpira 
#Si mostrar pero cuando ay muchas lineas de codigo es muy engorroso hacer estas pruebras asi
