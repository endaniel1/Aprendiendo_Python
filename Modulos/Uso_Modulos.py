#Aqui ara llamar desde un directorio q no esta en esta carpeta  se tiene q crear un archivo q nos servira
#como paquete q se creara dentro de la carpeta q en este caso es Calculos llamado __init__.py
#Esto dara a entender a python q esa carpeta es un paqueta y buscara por ay
#Despues para acceder a ella se coloca el nombre de la carpeta y como una clase se coloca . y el archivo q vamos a utilizar
#Y si se quiere utilizar una subcarpeta o sub directorio en este mismos se tiene q crear el archivo __init_.py para poder utilizarse de la misma manera
from Calculos.Calculos_Generales import *

dividir(4,2)