#Crear un programa en lenguaje de programación Python que le pregunte al usuario por una frase y una letra, y muestre en pantalla el número de veces que aparece la letra en la frase.

frase = str(input("Ingrese la frase: "))
letra = str(input("Ingrese la letra: "))

cantidadCaracteres = len(letra)

contador = 0
while contador<1:
    

    while cantidadCaracteres != 1:
        if cantidadCaracteres > 2 :
            print("ingresaste una frase debes ingresar una letra")
    
        letra = str(input("Ingrese una letra por favor: "))
        cantidadCaracteres=len(letra)

    contador = contador + 1

# for x in range (cantidadCaracteres):    
#     if cantidadCaracteres > 1:
#         print("ingresaste mas de una letra")        
        
#     letra = str(input("Ingrese otra letra: "))

#     cantidadCaracteres=len(letra)

mayusculaFrase=frase.upper()
mayusculaLetra = letra.upper()
# print(mayusculaLetra)
             
contador = 0

for x in mayusculaFrase:
    # print(frase)
    if x == mayusculaLetra:        
        contador = contador+1
        # print(contador)
    
print(f"la frase: {mayusculaFrase} tiene la letra: {mayusculaLetra}, repetidamente: {contador}")
        
        
    

