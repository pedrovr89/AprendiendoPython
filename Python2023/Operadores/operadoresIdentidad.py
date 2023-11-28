# Operadores de identidad (is, is not)
frutas1 = ["manzana","pera"]
frutas2 = ["manzana","pera"]
frutas3 = frutas1
print(frutas3 is frutas1)#true con la asignacion anterior pasan a ser el mismo objeto con nombre diferente
#añadimos un elemento
frutas3.append("naranja")
print(frutas3)
print(frutas1)#comparte el mismo objeto que frutas3
#is not
print(frutas1 is not frutas3)#false lo contrario que is