# for
# para iterar sobre elementos

colores = ["rojo","verde","azul"]

for color in colores:
    print(color)

cadena = "Hola mundo"

for caracter in cadena:
    print(caracter)

#range define una lista de numeros del 0 al 7 en este caso
range(0,8)
for numero in range(0,8):
    print(numero)
#una lista del 0 al 7 saltando de dos en dos
for numero in range(0,8,2):
    print(numero)

#break para parar el bucle. Range de esa forma crea una lista de 0 a 9
for numero in range(10):
    if (numero == 5):
        break
    print(numero)

#continue para romper la iteración actual
for numero in range(10):
    if (numero == 6):
        continue
    print(numero)

# doble for
for numero1 in range(4):
    for numero2 in range (3):
        print(numero1, numero2)
