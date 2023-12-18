media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3

class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self):
        print(f"Coche marca {self.marca}, color {self.color}, combustible {self.combustible} y cilindrada {self.cilindrada}")
