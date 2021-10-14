#Ingresar una palabra y que la muestre de manera inversa
#Crear un programa en lenguaje de programación Python que le pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.


palabra=input("Ingrese la Palabra: ")

#invertir cadena
cadenaInvertida=palabra[::-1]

#imprimo palabra por palabra
for x in cadenaInvertida:
    
    # print(x)
    print(x)

