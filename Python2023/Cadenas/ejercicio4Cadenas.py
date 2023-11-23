#Ejercicio 4
# Imprime por pantalla el texto "Introduce el primer número"
# Crear la variable "dato1" con el primer valor introducido en el paso anterior
# Imprime por pantalla el texto "Introduce el segundo número"
# Crear la variable "dato2" con el primer valor introducido en el paso anterior
# Convertir la variable "dato1" en una variable numérica denominada "numero1"
# Convertir la variable "dato2" en una variable numérica denominada "numero2"
# Crear la variable "suma" con la suma de "numero1" y "numero2"
# Convertir la variable "suma" en una variable de texto denominada "strSuma"
# Crear la variable "resultado" con la concatenación de "La suma es " y "strSuma"
# Imprimir el valor de "resultado"
print("Introduce el primer número")
dato1 = input()
print("Introduce el segundo número")
dato2 = input()
numero1 = int(dato1)
numero2 = int(dato2)
suma = numero1 + numero2
strSuma = str(suma)
resultado = "La suma es " + strSuma
print(resultado)