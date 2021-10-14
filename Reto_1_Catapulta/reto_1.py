#Entrada numero entero 
import math
bandera=True

while bandera:
    distancia=input("Ingrese la distancia: ")
    if distancia.isalpha()==True:
        print("Ingresaste un valor alfabetico")
    elif distancia.isdigit()==True:
        break
    elif distancia.isalnum()==True:
        print("Ingresaste un valor alfanumerico")


def tiro_p():
    distancia_p=distancia
    return distancia_p
def tiro_h():
    distancia_h=0
    distancia_h=(int(tiro_p())*2)+4
    return distancia_h
def tiro_l():    
    distancia_l=int(tiro_p())/5 + int(tiro_h())/5
    return distancia_l
def categoria():
    categoria_tiro_l =" "
    if int(tiro_l())>=0 and int(tiro_l())<=20:
        print("uno")
    elif int(tiro_l())>=21 and int(tiro_l())<=30:
        print("dos")
    elif int(tiro_l())>=31 and int(tiro_l())<=50:
        print("tres")
    else:
        print("cuatro")
    return categoria_tiro_l



print(tiro_p(),int(tiro_h()),int(tiro_l()))
print(categoria())