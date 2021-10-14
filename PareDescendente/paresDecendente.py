#Numero Pares decendentes


numero = int(input("Ingrese numero: "))



contador = 0

while numero>contador:
    
    if numero%2==0:
        print(f"numero par {numero}")
    # elif numero%2==1:
    #     print(f"numero impar {numero}")


    # numero=2*(numero) + 1        
    # print(f"Numero decendente {numero}")
    numero=numero-1 
    

print("fin")




