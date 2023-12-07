#Ejercicio 3
# Crear una variable "tupla" que sea una tupla de los siguientes nombres: Antonio, Pedro y María
# Mostrar el valor de la variable "tupla"
# Recoger un dato por teclado y almacenarlo en la variable "dato"
# Si el valor de "dato" está dentro de los valores de la variable "tupla", mostrar "Sí"
# Si el valor de "dato" no está dentro de los valores de la variable "tupla", mostrar "No"

tupla = ("Antonio", "Pedro", "María")
print(tupla)
dato = input("Introduce un dato: ")

if(dato in tupla):
    print("Sí")
else:
    print("No")