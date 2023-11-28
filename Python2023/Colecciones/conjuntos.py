# Conjuntos, colección de elementos desordenada, no hay índice para acceder a sus elementos
conjunto_colores = {"rojo","verde","azul"}#se define con llaves
print(conjunto_colores)
#recorrer con for
for color in conjunto_colores:
    print(color)
#no se puede acceder a una posición concreta
#conjunto_colores[1]#da error
#len para longitud
print(len(conjunto_colores))
#añadir elemento
conjunto_colores.add("negro")
print(conjunto_colores)
#borrar
conjunto_colores.remove("verde")
print(conjunto_colores)