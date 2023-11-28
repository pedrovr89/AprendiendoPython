#Operadores de pertenencia (in, not in)
frutas1 = ["manzana", "pera","naranja"]
frutas2 = "pera"
#in para verificar si un valor está incluida en una lista
print(frutas2 in frutas1)#true
#not in para verificar si no está incluido en una lista
print(frutas2 not in frutas1)#false
frutas3 = "melocoton"
print(frutas3 not in frutas1)#true