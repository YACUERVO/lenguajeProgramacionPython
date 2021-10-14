#Distancia entre dos puntos

import math

#Crear un programa en lenguaje de programación Python que reciba las coordenadas X y Y de dos puntos en el plano cartesiano, y calcule la distancia euclideana entre ellos. Las coordenadas pueden ser negativas. Se adjunta un link que explica como utilizar la función Raiz Cuadrada en Python, la cual solo se puede usar si escriben 'import math' al inicio del programa.

punto_Ax = int(input("Ingrese coordenada 'x' para el punto A: "))
punto_Ay = int(input("Ingrese coordena 'y' para el punto A: "))

punto_Bx= int(input("Ingrese coordenada 'x' para el punto B: "))
punto_By= int(input("Ingrese coordena 'y' para el punto B: "))

print(f"Punto A: ({punto_Ax},{punto_Ay})")
print(f"Punto B: ({punto_Bx},{punto_By})")

print("Distancia entre los dos puntos")

def distanciaDosPuntos():
    distancia = math.sqrt(((punto_Bx-punto_Ax)**2) + ((punto_By - punto_Ay)**2))
    return distancia


print(f"la distancia es:", distanciaDosPuntos())