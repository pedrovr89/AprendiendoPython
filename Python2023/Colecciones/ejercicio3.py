# Ejercicio 3
# Crear una variable "conjunto" que sea un conjunto con los valores 1,2,3,4 y 5
# Mostrar el valor de la variable "conjunto"
# Añadir los números 6,7,8 y 9 a la variable "conjunto"
# Mostrar ahora el valor de la variable "conjunto"
# Eliminar el número 9 de la variable "conjunto"
# Mostrar ahora el valor de la variable "conjunto"
# Verificar que tipo de dato es la variable "conjunto" mediante type()

conjunto = {1, 2, 3, 4, 5}
print(conjunto)

conjunto.add(6)
conjunto.add(7)
conjunto.add(8)
conjunto.add(9)

print(conjunto)

conjunto.remove(9)

print(conjunto)

print(type(conjunto))