#Herencia en python
    #Clase padre
class Persona:
    def __init__(self,nombre, edad):
        self._nombre = nombre
        self._edad = edad
    def __str__(self):     
        return (f"{self._nombre} {self._edad}")
    #Clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    #Para llamar los valores de los atributos
    def __str__(self):     
        return (f"Sueldo {self._sueldo} Empleado: {super().__str__()}")


empleado_1 =Empleado("Juan",28,1500)
print(empleado_1) 