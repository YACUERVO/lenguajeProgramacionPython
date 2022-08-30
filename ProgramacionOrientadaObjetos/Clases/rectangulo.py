class Rectangulo:
    def __init__(self,altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def area(self):
        return self.altura * self.ancho

    
"Crear objetos"

base = int(input("Ingrese la altura: "))
altura = int(input("Ingrese la ancho: "))

rectangulo = Rectangulo(base,altura)
print(f"Area de rectangulo: {rectangulo.area()}")
