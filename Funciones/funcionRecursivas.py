#Imprimir numeros de 5 a 1 de manera descente usando funciones recursivas. 

def funcioRecursiva(numeros):
    if numeros >= 1:
        print(numeros)
        funcioRecursiva(numeros-1)
    elif numeros == 0:
        return
    elif numeros <= 0:
        print("Valor incorrecto")


funcioRecursiva(0) 
    