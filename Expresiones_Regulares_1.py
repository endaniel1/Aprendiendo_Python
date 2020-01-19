#Practica de expresiones regulares
#Importamos aqui la clase re q es la q nos tine las expresiones regulares
import re
#Aqui creamos una cadena de texto sencilla
cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
#Aqui creamos un texto en el cual vamos a ir a buscar
textBuscador="Python"
#Aqui con la clase seach() de re, lo q hacemos es buscar el texto en la cadena
#se le pasa el texto a buscar y despues la cadena o string
textoEncotrado=re.search(textBuscador,cadena)

print(textoEncotrado.start())#start() lo q hace es dar la posion donde encuentra la palabra del inicio
print(textoEncotrado.end())#end() lo q hace es dar la posion donde encuentra la palabra del final para atras
print(textoEncotrado.span())#span() lo q hace es dar la posion donde encuentra la palabra del final para atras y desde inicio en un tupla

#Aqui mostramos cauntas palabras se encuentra con la clase findall()
#recive el texto a buscar y la cadena 
#y nos muestras en forma de una lista las palabras
print(re.findall(textBuscador,cadena))
print(len(re.findall(textBuscador,cadena)))#Aqui con len mostramos cuantas cantidades de palabras ay