#Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.


# cantidad=int((input("Cantidad de valores a sumar: ")))

# contador = 0

# while contador < cantidad:
#     numeros=input("Ingreso los valores: ")
          
#     contador=1


def suma(*valores):
    valores = list(valores)
    multiplicar = 1
    for valor in valores:
        multiplicar *= valor

    return multiplicar


print(f"la multiplicación de los valores",suma(5,3,5))