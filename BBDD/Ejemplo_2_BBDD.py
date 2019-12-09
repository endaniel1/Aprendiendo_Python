#AQUI IMPORTE pymysql q tuve q descargar la libreria en python porque como tengo xampp instalado mas facil 
import pymysql

#Aqui me conecto en la base de datos con la clase connect() q tiene pymysql
miConecion=pymysql.connect("localhost","root","","PrimeraBaseDatosPython")

#Aqui indicamos o preparamos un objeto(cursor) para los diferente metodos a utilizar
miCursor=miConecion.cursor()

'''
variosProductos=[

	("Camiseta",10,"Deportes"),
	("Jarrón",50,"Cerámica"),
	("Camion",20,"Juguetes"),

]
'''

#Aqui ejecutamos los q queremos hacer con la clase execute()
miCursor.execute("SELECT * FROM PRODUCTOS")

#Aqui creamos una varible en el cual nos guarde los datos q trae nuestra consulta 
#fetchall() lo q hace es traer los datos en forma de tupla
variosProductos=miCursor.fetchall()

#Aqui con un ciclo sencillo recorremos los datos q nos trae
for productos in variosProductos:	
	print("Nombre Del Productos:",productos[0],"Sección:",productos[2])


#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(%s,%s,%s)",variosProductos)

#Aqui confirmamos los cambios de nuestra base de datos con la clase commit()
miConecion.commit()

#Aqui desconectamos de nuestra base de datos
miConecion.close()