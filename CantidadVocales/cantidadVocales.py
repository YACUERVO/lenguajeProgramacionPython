#Crear un programa en lenguaje de programación Python que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

while True:
    palabra=input("Ingrese la palabra a verficar: ")
    palabra=palabra.lower()
    # print(palabra)

    if palabra.isdigit() == True:
        print("Error ingreso un numero")

    elif palabra.isalpha() == True:
        break

    elif palabra.isalnum() == True:        
        print("Error ingreso caracteres alfanumericos")




def cantidadVocales(palabra_1):
    a=0
    e=0
    i=0
    o=0
    u=0
    for item in palabra_1:        
        if item == "a":
            a=a+1
        if item == "e":
            e=e+1
        if item == "i":
            i=i+1
        if item == "o":
            o=o+1
        if item == "u":
            u=u+1
    
    
    if a > 1 or e > 1 or i>0 or o>1 or u>1:    
        print(f"la palabra {palabra_1} tiene: a: {a} e: {e} i:{i} o:{o} u:{u}")

# def mostrarCantidades(cantidadVocales):
#     if cantidadVocales > 1:
#         print(f"la palabra {palabra} tiene: {a}")




(cantidadVocales(palabra))
        
