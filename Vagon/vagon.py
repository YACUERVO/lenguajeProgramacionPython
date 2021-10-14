import math


area_Circulo =int(input("Ingrese el radio del circulo:  "))
lado = int(input("ingrese el lado B: "))
altura = int(input("ingrese el lado A: "))

def areaCirculo(x):
     area = 2*(math.pi*(x**2))
     return area

# def areaCirculo1(x):
#     area = 3.1416*(x*x)
#     return area

def areaLeteral(a,b):
    areaVagon = (a + b)
    return areaVagon

def area_Vagon():
    areaTotal=areaCirculo(area_Circulo) + areaLeteral(lado,altura)
    return areaTotal

# print(areaCirculo(area_Circulo))
# # print(areaCirculo1(area_Circulo))
# print(areaLeteral(lado,altura))

print("area total del carrito es: ", area_Vagon())




