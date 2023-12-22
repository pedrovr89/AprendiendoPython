# leer el fichero de texto
#nombre de fichero y tipo, r read
fichero = open("./Python2023/Ficheros_Texto/ficheroTexto.txt","r")

datos_fichero = fichero.read()
fichero.close()
print(datos_fichero)