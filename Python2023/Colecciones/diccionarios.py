# Diccionarios, colección de elementos indexados escritos entre llave y formado por pares clave valor
diccionario_colores = {"red":"rojo", "blue":"azul","yellow":"amarillo"}
print(diccionario_colores)
#acceder a la clave
print(diccionario_colores["red"])
#añadir elemento
diccionario_colores["black"] = "negro"
print(diccionario_colores)
#borrar valores
diccionario_colores.pop("yellow")
print(diccionario_colores)
del(diccionario_colores["black"])
print(diccionario_colores)
#recorrer con for
for color in diccionario_colores:#solo las claves
    print(color)
for clave,valor in diccionario_colores.items():
    print(clave,valor)