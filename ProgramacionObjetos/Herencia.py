class Herencia:
#Clase padre
    #Iniciar los atributos
    def __init__(self, nombre, edad):
        self._nombre=nombre
        self._edad=edad
    
    #para llamar el objeto
    def __str__(self):
        return f"Persona: nombre: {self._nombre} edad: {self._edad}"

    #medotos get = obtener y recuperar
    @property 
    def nombre(self):        
        return self._nombre          
    @property
    def edad(self):
        return self._edad

    #metodo set = colocar y modificar
    @nombre.setter
    def nombre(self, nombre):       
        self._nombre = nombre
    @edad.setter
    def edad(self,edad):
        self._edad=edad

#Heredar los metodos y los atributos de la clases padre
class Persona(Herencia):

    #Iniciar los atributos
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo=sueldo

    #Heredar metodo str para mostrar datos
    def __str__(self):
        return f"{super().__str__()} Sueldo: {self._sueldo}"

    #Metodo get = obtener y recuperar
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo=sueldo


# Persona_1 = Persona("Yamith","30",2500000)
# print(Persona_1.nombre)
# print(Persona_1.edad)
# print(Persona_1.sueldo)