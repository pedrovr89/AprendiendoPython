# While
# hacemos un conjunto de acciones mientras se cumple la condicion

valor = 1
fin = 10
while (valor < fin):
    print(valor)
    valor += 1

# break
valor = 1
fin = 10
while (valor < fin):
    print(valor)
    valor += 1
    if (valor == 5):
        break

# continue
valor = 1
fin = 10
while (valor < fin):
    valor += 1
    if (valor == 6):
        continue
    print(valor)
    
