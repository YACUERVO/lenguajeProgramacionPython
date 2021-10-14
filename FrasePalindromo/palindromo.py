#Crear un programa en lenguaje de programación Python que pida al usuario una frase y muestre como resultado True si la frase es un Palindromo, y False en caso contrario.



while True:

    frasePolindromo = input("Ingrese la palabra a verificar: ")  #Convertir la cadena de texto en minuscula 
    # print(frasePolindromo)

    if frasePolindromo.isdigit() == True:#validación si la variable frasePolindroma contiene numeros
        print("Error: El texto ingresado es un número")     
    elif frasePolindromo.isalpha() == True:#validación si la variable frasePolindroma si es una cadena de texto entonces realice un freno en el while y continue el programa
        # print("Continue")
        break
    elif frasePolindromo.isalnum() == True:
        print("Cadena de texto con caracteres y numeros")##validación si la variable frasePolindroma, contiene un caracter y numero revueltos

# print(frasePolindromo)

def frase_polindromo(frase):
    FraseLista=frase.lower()
    FraseLista=list(FraseLista)
    # print(fraseLista)
    FraseNueva=[]
    

    for item in range(len(FraseLista)-1,-1,-1):#interrar desde el utlimo elemento hasta el primero
        FraseNueva.append(FraseLista[item])    

    FraseNueva="".join(FraseNueva).lower()
    FraseNueva_Minuscula=list(FraseNueva)  
    # print(FraseNueva)   

    for item_1, item_2 in zip(FraseLista,FraseNueva):
        if FraseLista[0] == FraseNueva_Minuscula[0] and FraseLista[1] == FraseNueva_Minuscula[1] and FraseLista[2] == FraseNueva_Minuscula[2] and FraseLista[3] == FraseNueva_Minuscula[3]:
            print("Palabra Palindroma")
            break
        else:
            print("palabra NO Palindroma")
            break
            


    # print(FraseNueva_Minuscula)
    # print(FraseLista)
    




frase_polindromo(frasePolindromo)