class Vehiculo:
    #Defino los atributos
    def __init__(self,color,ruedas):
        self._color=color
        self._ruedas=ruedas

    #Mostrar detalles del objeto
    def __str__(self):
        return f"Color: {self._color} Ruedas: {self._ruedas}"

    #Metodo get: Mostrar
    @property
    def color(self):
        return self._color
    @property
    def ruedas(self):
        return self._ruedas

    #Metodo setter: Modificar
    @color.setter
    def color(self,color):
        self._ruedas=color
    @ruedas.setter
    def ruedas(self,ruedas):
        self._ruedas=ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self._velocidad=velocidad

    #Mostrar detalles del objeto
    def __str__(self):
        return f"{super().__str__()} Velocidad: {self._velocidad}"

    #Metodo get
    @property
    def velocidad(self):
        return self._velocidad
    
    #Metodo set
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self._tipo=tipo

    def __str__(self):
        return f"{super().__str__()} Tipo: {self._tipo}"
    
    #metodo get
    @property
    def tipo(self):
        return self._tipo
    
    #metodo set
    @tipo.setter
    def tipo(self,tipo):
        self._tipo=tipo

Vehiculo_1=Vehiculo("Rojo",2)
print(Vehiculo_1)

Coche_1=Coche("verde",4,"180km")
print(Coche_1)

Bicicleta_1=Bicicleta("Amarillo","2","Urbano")
print(Bicicleta_1)