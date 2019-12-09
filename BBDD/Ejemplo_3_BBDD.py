import pymysql
#Aqui me conecto en la base de datos con la clase connect() q tiene pymysql
miConexion=pymysql.connect("localhost","root","","PrimeraBaseDatosPython")

#Aqui indicamos o preparamos un objeto(cursor) para los diferente metodos a utilizar
miCursor=miConexion.cursor()

#Aqui creamos un tabla llamada productos
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
		ID INTEGER PRIMARY KEY AUTO_INCREMENT,	
		NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
		PRECIO INTEGER,
		SECCION VARCHAR(20)
	)
''')

#Aqui creamos una tupla q tiene varios productos a insertar
variosProductos=[

	("Camiseta",10,"Deportes"),
	("Jarrón",50,"Cerámica"),
	("Camion",20,"Juguetes"),
	("Destornillador",25,"Ferreteria"),
	("Jarrónes",50,"Cerámica"),

]

#Aqui se inserta los productos con la clase executemany() y se le pasa null porque con el id es autoincrementable mysql lo rellena por defecto
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,%s,%s,%s)",variosProductos)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05','Tren',15,'Jugueteria')")

#Aqui confirmamos los cambios de nuestra base de datos con la clase commit()
miConexion.commit()

#Aqui desconectamos de nuestra base de datos
miConexion.close()