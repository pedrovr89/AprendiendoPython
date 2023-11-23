#Imprimir variables en una cadena
nombre = "Pedro"
edad = 34
#concatenar
print("Buenos días " + nombre)
#format
print("Buenos días {}, feliz {} cumpleaños".format(nombre,edad))
#formatear número
resultado = 3.333333333
print("El resultado es {r:1.3f}".format(r = resultado))
#f-strings a partir de version 3.6
print(f"Buenos días {nombre}, feliz {edad} cumpleaños")