from abc import ABC, abstractmethod

class HerenciaMultiple(ABC):
    #Validaciones en la inicializacion de variables
    def __init__(self, ancho,alto):
        if self._validar_valor(ancho):
            self._ancho=ancho
        else:
            self._ancho=0   
            print(f"Valor erroneo ancho: {ancho}") 
        if self._validar_valor(alto):    
             self._alto=alto
        else:
            self._alto=0
            print(f"Valor erroneo alto: {alto}") 

    def __str__(self):
        return f'''
        Ancho: {self._ancho}
        Alto:  {self._alto}'''

    @property
    def ancho(self):
        return self._ancho
    @property
    def alto(self):
        return self._alto

    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho=ancho
        else:
            print(f"Valor erroneo ancho: {ancho}")
            
    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self.alto=alto
        else:
            print(f"Valor erroneo alto: {alto}")
    
    def _validar_valor(self, valor):    
        return True if 0 < valor < 10 else False

    #Para que no se instacia la clase padre este metodo permite obligar a las clases hijas que se realce la funcionalidad
    @abstractmethod
    def calcular_area(self):
        pass


class Color:
    def __init__(self,color):
        self._color=color

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color
    def __str__(self):
        return f'''
        Color: {self._color}
        '''

class Cuadrado (HerenciaMultiple,Color):
    #Forma de inicilizar la herencia multiple a una clase hija
    def __init__(self, ancho, alto, color):
        HerenciaMultiple.__init__(self,ancho,alto)
        Color.__init__(self,color)

    def __str__(self):
        return f"{HerenciaMultiple.__str__(self)} {Color.__str__(self)}"
        

    def calcular_area(self):
        return self._alto*self._ancho

    

class Rectangulo(HerenciaMultiple,Color):
    def __init__(self, ancho, alto,color):
        HerenciaMultiple.__init__(self,ancho,alto)
        Color.__init__(self,color)
    def __str__(self):
        return f"{HerenciaMultiple.__str__(self)} {Color.__str__(self)}"
    
    def calcular_area(self):
        return self._alto*self._ancho


Cuadrado_1=Cuadrado(-5,9,"negro")

print("Creacion del Cuadrado".center(50,'-'))
print(Cuadrado_1)
Cuadrado_1.ancho=15
#Acceder al metodo calcular area
print(f"El area del cuadrado es : {Cuadrado_1.calcular_area()}")
# Cuadrado_1.ancho
# print(Cuadrado_1)
Rectangulo_1=Rectangulo(4,9,"Rojo")
print("Creacion del Rectangulo".center(50,'-'))
print(Rectangulo_1)
#Acceder al metodo de calcular area
print(f"El area del rectagulo es: {Rectangulo_1.calcular_area()}")

#No se puede intaciar una clases abstracta
#figura=HerenciaMultiple()

#MRO - Methon Resolution Order, para validar las clases de manera ordenada
print(Cuadrado.mro())