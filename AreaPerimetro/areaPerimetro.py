#Area y perimetro de un carrito
#Crear un programa en lenguaje de programación Python que calcule y muestre en la consola el area de un carrito compuesto de dos circulos y un rectangulo. El programa debe recibir 3 datos de entrada: El alto y ancho del rectangulo, y el radio del circulo. Se prefiere que el programa use Funciones en su construcción.

import math

rectanguloAltura_A = int(input("Ingrese altura rectangulo A: "))
rectanguloAncho_A = int(input("Ingrese ancho rectangulo A: "))

rectanguloAltura_B = int(input("Ingrese altura rectangulo B: "))
rectanguloAncho_B = int(input("Ingrese ancho rectangulo B: "))

Radio_A =int(input("Ingrese el radio del circulo A: "))
Radio_B =int(input("Ingrese el radio del circulo B: "))



def areaRectangulo(a,b):
    area = a*b 
    return area

def perimetroRectangulo(a,b):
   perimetroRectangulos = ((2*a) + (2*b))
   return perimetroRectangulos


def areaCirculo(r):
    areaCirculo = math.pi * r**2
    return areaCirculo

def perimetroCirculo(r):
    perimetro = 2 * math.pi * r
    return perimetro

def total():
    total_perimetros = perimetroCirculo(Radio_B) +perimetroCirculo(Radio_A) + perimetroRectangulo(rectanguloAncho_A,rectanguloAltura_A) + perimetroRectangulo(rectanguloAltura_B,rectanguloAncho_B)
    print("el total de los perimetors", total_perimetros)

    
print("Area Rectangulo A: ",areaRectangulo(rectanguloAltura_A,rectanguloAncho_A))    
print("Perimetro Rectangulo A: ", perimetroRectangulo(rectanguloAltura_A,rectanguloAncho_A))
print("Area Rectangulo B: ", areaRectangulo(rectanguloAltura_B,rectanguloAncho_B))
print("Perimetro Rectangulo B: ", perimetroRectangulo(rectanguloAltura_B,rectanguloAncho_B))

print("Area Circulo A: ",areaCirculo(Radio_A))
print("Perimetro Circulo A: ",perimetroCirculo(Radio_A))
print("Area Circulo B: ", areaCirculo(Radio_B))
print("Perimetro Circulo B: ", perimetroCirculo(Radio_B))

total()


