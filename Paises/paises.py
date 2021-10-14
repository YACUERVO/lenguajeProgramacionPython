#Desarrollar un algoritmo para indicar que pais supere en poblacion de acuerdo al año

pais_A = 25000000
pais_B = 18000000

contador = 1

# def poblacionA():
#     pais_A1 = pais_A * 1.02
#     return pais_A1



# def poblacionB():
#     pais_B1 = pais_B * 1.03
#     return pais_B1

año=2021


while contador <=año:
    def poblacionA():
        pais_A1 = pais_A * 1.02
        return pais_A1
    

    def poblacionB():
        pais_B1 = pais_B * 1.03
        return pais_B1

    pais_A = poblacionA()
    pais_B = poblacionB()

    if pais_B > pais_A:
        almacene = año
        print(f"poblacion B: {int(pais_B)} Supero a Poblacion A: {int(pais_A)}")
        print(almacene)

        break
    # else:

    #     print("poblaciones desiguales", int(poblacionA())  ,  int(poblacionB()))
    año+=1
    contador+= 1



