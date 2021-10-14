#Tipos de Triangulos
#Crear un programa en lenguaje de programación Python que reciba la longitud de los 3 lados de un triángulo e indique si es equilátero (tres lados iguales), isósceles (sólo dos lados iguales) o escaleno (tres lados diferentes).

Longitud_A = int(input("Ingrese la longitud del triangulo lado A: "))
Longitud_B = int(input("Ingrese la longitud del triangulo lado B: "))
Longitud_C = int(input("Ingrese la longitud del triangulo lado C: "))

def tipoTriangulo(a,b,c):   
    if  (a==b!=c) or (a==c!=b) or (c==b!=a):
        print("triangulo Isosceles")
    elif ( a== b == c):
        print("Triangulo Equilatero")
    elif ( a != b and b != c and a != c):
        print("Triangulo Escaleno")


tipoTriangulo(Longitud_A,Longitud_B,Longitud_C)
