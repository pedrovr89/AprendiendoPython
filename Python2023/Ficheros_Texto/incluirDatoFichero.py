#Open para incluir datos en un fichero con la a y t para texto
fichero = open("./Python2023/Ficheros_Texto/ficheroTexto.txt","at")
cadena_para_incluir = "\nEsta es la tercera fila del fichero"
fichero.write(cadena_para_incluir)
fichero.close()