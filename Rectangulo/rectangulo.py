#Crear un programa en lenguaje de programación Python que reciba las coordenadas X y Y del centro de un rectangulo en el plano cartesiano, asi como su ancho y su alto, luego reciba las coordenadas A y B de un punto llamado AB. El programa debe mostrar True si el punto AB se encuentra dentro del rectangulo, y False si se encuentra por fuera. Las coordenadas pueden ser negativas.

cordenada_x = int(input("Ingrese coordenada x: "))
cordenada_y = int(input("Ingrese coordenada y: "))


altura=int(input("altura: "))
ancho=int(input("ancho : "))

punto_A=int(input("A: "))
punto_B=int(input("B: "))


def rectagulo ():
    if punto_A - cordenada_x <= ancho/2 and punto_B - cordenada_y <= altura/2 and cordenada_x - punto_A <= ancho/2 and cordenada_y - punto_B<=altura :
     return ("True")
    else:
     return ("false")



print(rectagulo())

