class Area:

    def __init__(self,base,altura):
    #definimos nuestros atributos o variables para utlizar en los metodos
        self.base=base
        self.altura=altura
    #metodo para calcular el rectangulo
    def areaRectangulo(self):
        area = self.base * self.altura
        return area


#creo las variables 
base_1=int(input("Ingrese la base: "))
altura_1=int(input("Ingrese la altura: "))

#creo objeto para darle los argumentos 
Area_1=Area(base_1,altura_1)

#imprimo el area del rectangulo con el metodo
print(f"El area del rectangulo es: {Area_1.areaRectangulo()}")



