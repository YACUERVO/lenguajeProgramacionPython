#Programa vocales
#Crear un programa en lenguaje de programación Python que solicite al usuario ingresar una letra y, si es una vocal, muestre el mensaje “La letra ingresada es VOCAL”, de lo contrario debe mostrar "La letra ingresada NO ES VOCAL". Se debe validar que el usuario ingrese sólo un caracter, es decir, si ingresa más de un caracter, debe mostrar "Por favor ingresar solo una letra".

a = str("a")
e = str("e")
i = str("o")
o = str("o")
u = str("u")

letra = str(input("Ingrese una letra: "))

x=len(letra)

def no_vocal():
    if letra !=a or letra !=a or letra!=e or letra!=i or letra!=o or letra !=u:
            print("La letra ingresada NO ES VOCAL")


def vocal():
    if x > 1:
        print("ingresaste una palabra")
        ingrese_otra()  
    elif letra ==a or letra==e or letra==i or letra==o or letra==u:
        print(f"La letra ingresada es VOCAL")
    else:
        no_vocal() 

 
def ingrese_otra():
    letra1 = input("ingresa una vocal nuevamente: ")
    y=len(letra1)
    if y > 1:
       vocal()

    if y==1:
        # print(f"ingresaste una palabra que contiene {y}, caracter")
        # print(f"la letra escogida es {letra1}")
        if letra1 ==a or letra1==e or letra1==i or letra1==o or letra1==u:
            print("La letra ingresada es VOCAL")
        else:
            no_vocal()

        # print(type(letra1))
    return letra1

vocal()


















