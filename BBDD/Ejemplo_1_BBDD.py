#import sqlite3 #Tambien funciona pero lo unico q ay q tener un visor de base de datos
#AQUI IMPORTE pymysql q tuve q descargar la libreria en python porque como tengo xampp instalado mas facil 
import pymysql

#Aqui me conecto en la base de datos con la clase connect() q tiene pymysql
#Se le pasa donde estamos trabajando en este caso en forma local 
#el usuario q lo utiliza en este caso root
#la contraseña p password , finalmente el nombre de la base de datos
miConecion=pymysql.connect("localhost","root","","PrimeraBaseDatosPython")

#Aqui indicamos o preparamos un objeto(cursor) para los diferente metodos a utilizar
miCursor=miConecion.cursor()

#Aqui ejecutamos los q queremos hacer con la clase execute()
#le pasamos el comando SQL q queramos realizar
#Aqui este comando lo q hace es crear una tabla 
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")

#Aqui confirmamos los cambios de nuestra base de datos con la clase commit()
miConecion.commit()

#Aqui desconectamos de nuestra base de datos
miConecion.close()