#Clase padre
class Vehiculo:
    #Atributos
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas =ruedas

    #Imprimir
    def __str__(self):
        return f"Color {self.color} Ruedas {self.ruedas} "

#Claase hija
class Coche(Vehiculo):
    #Herencia de a clase Padre
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    #Herencia de la clase Hija para imprimir
    def __str__(self):
        return super().__str__() +  "Velocidad(km/hr): " + str(self.velocidad)

class Bisicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + "Tipo: " + str(self.tipo)

#Cream,o un objeto de la clase padre
vehiculo = Vehiculo("Rojo", 4)
print(vehiculo )


#Creamos un objeto de la calse hija
coche =Coche("violeta", 4, "55km")
print(coche)

#Creamos un objeto de la clase hija 
bisicleta =Bisicleta("Negro", 2,"Urbanos")
print(bisicleta)