class Cubo:
    def __init__(self,ancho,altura,profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcularVolumen(self):
        return self.ancho* self.altura*self.profundidad

"Variables"
ancho=int(input("ingrese el ancho: "))
altura=int(input("Ingrese el altura: "))
profundidad=int(input("Profundidad: "))

"Crear objetos"
cubo = Cubo(ancho,altura,profundidad)
print(f"El volumen es : {cubo.calcularVolumen()}")

