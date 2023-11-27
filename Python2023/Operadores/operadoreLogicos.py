# Operadores lógicos (and, or, not)
numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8

print(numero1 > numero2)#true
print(numero3 < numero4)#true
#and ambas tienen que ser ciertas para que sea true
print(numero1 > numero2 and numero3 < numero4)#true
#or si cumple alguna de las condiciones es true
print(numero1 > numero2 or numero3 > numero4)#false
#not para evaluar lo contrario, negar la condición
print(numero3 > numero4)#false
print(not numero3 > numero4)#true