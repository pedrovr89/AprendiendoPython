#Listas, colección de elementos que se puede modificar
colores = ["rojo","amarillo","verde"]
print(colores)
#modificar un elemento
print(colores[0])
colores[1] = "azul"
print(colores)
#len longitud lista
print(len(colores))
#añadir elemento
colores.append("naranja")
print(colores)
#borrar valor
colores.remove("rojo")
print(colores)
#recorrer lista
for color in colores:
    print(color)
#para limpiar lista
colores.clear()
print(colores)