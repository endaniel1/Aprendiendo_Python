import pymysql
#Aqui me conecto en la base de datos con la clase connect() q tiene pymysql
miConexion=pymysql.connect("localhost","root","","PrimeraBaseDatosPython")

#Aqui indicamos o preparamos un objeto(cursor) para los diferente metodos a utilizar
miCursor=miConexion.cursor()

#Aqui se actualiza un registro con la clase execute()
#Aqui le decimos q cambie el precio del arituclo camion
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Camion'")

#Aqui se elimina un registro con la clse execute()
#Aqui le decimos q elimine el registro numero 5 osea q el id sea 5
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


#Aqui confirmamos los cambios de nuestra base de datos con la clase commit()
miConexion.commit()

#Aqui desconectamos de nuestra base de datos
miConexion.close()