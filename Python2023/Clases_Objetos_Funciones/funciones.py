# Funciones

def saludar():
    print("Buenos días")

saludar()

def saludar(nombre):
    print(f"Buenos días {nombre}")

nombre = "Pedro"
saludar(nombre)

def sumar(numero1, numero2):
    suma = numero1 + numero2
    return suma

print(sumar(3,8))

# Paso de valor por referencia
colores = ["rojo","verde","azul"]

def incluir_color(colores, color):
    colores.append(color)

print(colores)
incluir_color(colores, "negro")
print(colores)