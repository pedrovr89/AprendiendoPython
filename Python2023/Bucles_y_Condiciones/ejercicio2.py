# Ejercicio 2
# Creamos una variable "nota" que tenga el valor 4.5
# Creamos una variable "trabajo_realizado" que tenga el valor "sí"
# Calcular el valor de la variable "nota_final", teniendo en cuenta que, si la nota es mayor o igual a 4 y el 
# calor de la varialbe "trabajo_realizado" es igual a "sí", entonces "nota_final" será igual a "aprobado", en caso
# contrario será igual a "Suspenso"

nota = 4.5
trabajo_realizado = "si"

if (nota >= 4 and trabajo_realizado.upper() == "SI"):
    nota_final = "Aprobado"
else:
    nota_final = "Suspenso"
print(nota_final)