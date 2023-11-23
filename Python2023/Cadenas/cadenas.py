#cadenas
#Se pueden escribir entre comillas simples o dobles
cadena = "Hola mundo"
#son secuencia de caracteres
#H o l a   m u n d o
#0 1 2 3 4 5 6 7 8 9
print(cadena[5])
#para la ultima posicion se usa -1
print(cadena[-1])
#para un substring [inicio:fin(no incluido)]
print(cadena[2:7])
#si omitimos uno hasta el final
print(cadena[2:])
#concatenacion
cadena2 = "!!!"
cadena3 = cadena + cadena2
print(cadena3)