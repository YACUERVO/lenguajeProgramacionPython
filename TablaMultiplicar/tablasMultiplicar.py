#Tablas de Multiplicar
#Crear un programa en lenguaje de programación Python que reciba un número entero positivo y muestre por pantalla la tabla de multiplicar de ese número. Si el número ingresado no es entero ni positivo, mostrar un mensaje de error y solicitar el ingreso de un número nuevo, de manera indefinida, hasta recibir el número correcto.


# Ej. Si el usuario ingresa el número 20, el programa debe mostrar la tabla de multiplicar en el siguiente formato:


# | 20 x 1   = 20   |
# | 20 x 2   = 40   |
# | 20 x 3   = 60   |
# | 20 x 4   = 80   |
# | 20 x 5   = 100 |
# | 20 x 6   = 120 |
# | 20 x 7   = 140 |
# | 20 x 8   = 160 |
# | 20 x 9   = 180 |
# | 20 x 10 = 200 |

numero = input("ingrese el numero a multiplicar: ")



contador = 0
while contador < 1:      
    while True: 
        if numero.isalpha():
            numero = input("ingreso un string tiene que ingresasr un numero: ")                    
        elif int(numero) < 0:
            print("ingresaste un numero negativo")
            numero=input("ingresa nuevamente un numero positivo: ")
        elif int(numero)>0:       
            print("ingresaste un numero correcto") 
            break     

    contador=+1

numero = int(numero)
# print(type(numero))


for x in range(1,11,1):
    # print(x)
    resultado = numero * x

    print(f"| {numero} X {x} = {resultado} |")
