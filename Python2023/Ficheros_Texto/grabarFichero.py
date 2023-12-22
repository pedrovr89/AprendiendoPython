# Grabar fichero
# con Open con el modo w para escribir y t de texto
fichero = open("./Python2023/Ficheros_Texto/fichero_para_grabar.txt","wt")
texto_fichero = "Hola, esta es la línea que vamos a grabar en el fichero"

fichero.write(texto_fichero)
fichero.close()