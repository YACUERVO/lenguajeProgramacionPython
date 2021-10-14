
numeros=int(input("Ingrese un numero: "))

def funcioRecursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero * funcioRecursiva(numero-1)

print(f"el factorial {numeros} es ", funcioRecursiva(numeros))

def numeroDesendentes(numero):
    if numero >= 1:
        print(numero)
        numeroDesendentes(numero-1)

   

numeroDesendentes(numeros)