# Ejercicio 1
# Crear una clase "Coche" que tenga estos atributos:
# marca, color, combustible y cilindrada

# Crear la funcion "__init__" que asigna los parametros de la clase a los atributos de la clase

# Crear otra función "mostrar_caracteristicas" que mediante print muestre por pantalla
# las caracteristicas (o atributos) que tiene el Coche

# Crear un objeto "coche1" de la clase "Coche" con los atributos "Opel","rojo","gasolina","1.6"
# Ejecutar la función "mostrar_caracteristicas" del objeto "coche1"

class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self):
        print(f"Coche marca {self.marca}, color {self.color}, combustible {self.combustible} y cilindrada {self.cilindrada}")

coche1 = Coche("Opel","rojo","gasolina","1.6")

coche1.mostrar_caracteristicas()