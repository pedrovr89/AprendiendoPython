# Clases y objetos. Programación orientada a objetos. POO
class ClaseSilla:
    color = "Blanco"
    precio = 100

objetoSilla1 = ClaseSilla()

print(objetoSilla1.color)

objetoSilla2 = ClaseSilla()
objetoSilla2.color = "Verde"
objetoSilla2.precio = 120

print(objetoSilla2.color)

class Persona:
    #metodo constructor. self hace referencia a los atributos de la clase
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Juan", 37)

print(persona1.nombre)
persona1.saludar()