# Ejercicio 1
# Crea un diccionario con los siguientes pares de valores
#     manzana, apple
#     naranja, orange
#     platano, banana
#     limon, lemon

# Muestra la traducción para la palabra "naranja"
# Añade un elemento nuevo con "piña" y "pineapple"
# Haz un bucle para mostrar todos los elementos del diccionario

frutas = {"manzana":"apple","naranaja":"orange","platano":"banana","limon":"lemon"}

print(frutas["naranaja"])

frutas["piña"] = "pineapple"

for clave, valor in frutas.items():
    print(f"{clave} en inglés es {valor}")