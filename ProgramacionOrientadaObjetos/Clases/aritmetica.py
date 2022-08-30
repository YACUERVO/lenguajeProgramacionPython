class Aritmetica:
    """
    Clase artimetica para realizar las operaciones de sumar, restar etc
    """
    def __init__(self,numero_1,numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def sumar(self):
        return self.numero_1 + self.numero_2

    def restar(self):
        return self.numero_1 - self.numero_2

    def multiplicar(self):
        return self.numero_1 * self.numero_2
    
    def divir(self):
        return self.numero_1 / self.numero_2
    

"Crear Obejtos"
artimetica = Aritmetica(5,3)
print(f"Suma {artimetica.sumar()}")
print(f"Restar {artimetica.restar()}")
print(f"Multiplicar {artimetica.multiplicar()}")
print(f"Dividir {artimetica.divir():.2f}")

