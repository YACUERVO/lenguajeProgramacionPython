#Capital de Inversion
#Crear un programa en lenguaje de programación Python que pregunte al usuario una cantidad de dinero a invertir, un porcentaje de interés anual y un número de años, y muestre por pantalla el valor del capital que se tendria cada año que dure la inversión.


#El programa debe validar que la cantidad de dinero sea un valor real positivo, que el porcentaje anual sea ingresado en formato percentil y no en formato decimal (Ej: Cincuenta porciento debe ser ingresado como 50, no como 0.5), y que el número de años sea entero positivo, de lo contrario, el programa debe solicitar nuevamente, y de manera indefinida, los valores que hayan sido ingresados incorrectamente.


cantidadInvertir=int(input("cantidad de dinero a invertir: "))

#validar valor positivo del dinero a invertir

contador = 0
while contador < 1:
    while cantidadInvertir < 0:
        print("Ingresaste un valor negativo")
        cantidadInvertir = int(input("ingresaste un valor entero positivo para invertir: "))           

    contador+=1

#validar que el interes sea un entero y no un float

# interesAnual=input("porcentaje de interes anual: ")

def entero():
    interesAnual=0    
    while True:
        interesAnual = input("Ingresa un valor entero para el interes anual: ")
        try:
            interesAnual = int(interesAnual)
            return interesAnual
        except (ValueError):
            print("ingresaste un valor decimal")

x=entero()
# print(type(x))
         
#validar que el numero de años sea entero positivo
numeroAños=int(input("numero de años: "))

contador = 0
while contador<1:
    while numeroAños < 0:
        print("los años son enteros positivos")
        numeroAños = int(input("Ingrese años nuevamnete: "))
    contador+=1

# print(type(numeroAños))

# print(cantidadInvertir)
# print(x)
# print(numeroAños)



total_inversion = ((cantidadInvertir * (x/100)) * numeroAños) + cantidadInvertir
y = int(total_inversion)



print("El total de inversion es ", y)