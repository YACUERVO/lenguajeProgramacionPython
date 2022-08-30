#ABD = Abstract base clase
from abc import ABC, abstractmethod

class FiguraGeometrica:
    #Iniciando las variables
    def __init__(self,ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo ancho {ancho}")
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo alto {alto}")

    #Metodo GET
    @property
    def ancho(self):
        return self._ancho
    @property
    def alto(self):
        return self._alto
    
    #Metodo SET
    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho {ancho}")
    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo ancho {alto}")
    #Metodo para Imprimir
    def __str__(self):
        return f'''
        Figura Geometrica: 
            Ancho: {self._ancho}
            Alto: {self._alto}'''
    
   #Clases abstractas
    @abstractmethod
    def calcularAreas(self):
        pass
    
    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False

class Color:
    def __init__(self,color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color

    def __str__(self):
        return f'''
            Color: {self._color}'''


class Cuadrado(FiguraGeometrica,Color):

    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
    
    def calcularAreas(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f'''
            {FiguraGeometrica.__str__(self)} {Color.__str__(self)}
        '''
class Rectangulo(FiguraGeometrica,Color):

    def __init__(self,ancho,alto,color):
        #Llamar el metodo inicializado de la clase padre
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)

    def calcularArea(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"

print("Creacion objeto cuadrado".center(50,'-'))    
cuadrado = Cuadrado(5,"Amarillo")
# print(cuadrado.calcularAreas())
# print(cuadrado.color_1())
print(cuadrado)
cuadrado.ancho=-10
print(cuadrado)

#Crear un objeto de tipo rectangulo
rectangulo = Rectangulo(5,2,"Rojo")
print(f"Area Rectangulo: {rectangulo.calcularArea()}")


#MRO - METHOD RESOLUTION ORDER
#Metodo para verificar cuales son las clases en priorización 
# print(Cuadrado.mro())