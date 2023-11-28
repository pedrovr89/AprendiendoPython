#Ejercicio 3
# Crear una variable "numeros" con la lista de los números del 1 al 10 (ambos incluidos)
# Mostrar el valor de la variable "numeros"
# Recoger un dato del teclado y almacenarlo en la variable "dato"
# Convertir "dato" en nuérico y almacenarlo en la variable "numero"
# Si el valor de "numero" está en la lista de números, mostrar el mensaje "Sí"
# Si el número introducido no está en la lista de números, mostrar el mensaje "No"
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
dato = input("Introduce un número:")
numero = int(dato)
if (numero in numeros):
    print("Sí")
if (numero not in numeros):
    print("No")