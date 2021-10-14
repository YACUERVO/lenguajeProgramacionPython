#Variables 
#Crear un programa en lenguaje de programación Python que, usando variables de tipo float y operaciones aritmeticas como la multiplicacion y la división, calcule la fuerza de gravedad entre dos cuerpos usando la Ley de Gravitación Universal de Isaac Newton, y la muestre en la consola de salida. Los valores de entrada son la constante de gravitación universal, masa del cuerpo 1, masa del cuerpo 2 y la distancia entre los dos.

masa1 =int(input("ingrese la masa 1: "))
masa2 =int(input("ingrese la masa 2: "))
ingreseDistanci=int(input("ingrese distancia: "))
distancia = pow(ingreseDistanci,2);

#Constante de gravitacion universal
G: float = 6.67384 * pow (10,-11);

#Ley de gravitacion Universal
F = (G*((masa1*masa2)/distancia))




print(F);

