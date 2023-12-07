# Ejercicio 4
# Crear una variable "diccionario" con los pares de valores siguientes
#     clave = uno   valor = one
#     clave = dos valor = two
#     clave = tres    valor = three
# Mostrar por pantalla el valor de la variable "diccionario"
# Añadir un nuevo elemento al diccionario
#     clave = cuatro  valor = four
# Mostrar ahora el valor del diccionario
# Recoger un valor del diccionario
# Recoger un valor introducido por teclado y almacenarlo en "dato"
# Utilizar "dato" como clave del diccionario para recuperar su valor
diccionario = {"uno": "one", "dos": "two", "tres": "three"}
print(diccionario)
diccionario["cuatro"] = "four"
print(diccionario)
print(diccionario["dos"])
dato = input("Introduzca un valor: ")
if(dato in diccionario.keys()):
    print(diccionario[dato])
else:
    print("No existe la clave")