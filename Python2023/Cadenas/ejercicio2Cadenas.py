#Ejercicio 2
# Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
# Crear una variable "longitud" que contiene la longitud de la variable "cadena"
# Crear una variable "strLongitud" que tenga el valor de la "longitud" pero convertida a cadena
# Crear una variable "mayusculas" que contiene la variable "cadena" en mayusculas
# Crear una variable "resultado" que concatene "mayusculas" con el texto " tiene longitud de " y "strLongitud"

cadena = "Esto es un texto de ejemplo"
print(cadena)
longitud = len(cadena)
print(longitud)
strLongitud = str(longitud)
print(strLongitud)
mayusculas = cadena.upper()
print(mayusculas)
resultado = mayusculas + " tiene longitud de " + strLongitud
print(resultado)