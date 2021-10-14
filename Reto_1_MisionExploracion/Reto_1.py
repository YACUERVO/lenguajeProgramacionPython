#Reto 1: Grupo P90
#Yamith Arley Cuervo Corredor

#variable global
distancia = int(input (" "))

#Distancia
def distancia_inicial(x):    
    return x

#Funcion peso de la carga en toneladas
def peso(x):
    peso = ((2*x + 4));
    return peso

#Funcion cantidad de combustibles en gigalitros requeridos para el viaje

def combustible():
    combustible = int((peso(distancia) + distancia)/5)
    return combustible



#Cantidad de cohetes
def CantidadCohetes():
    cantidad_combustible=combustible()
    if cantidad_combustible <= 20:
        return ("uno")
    elif cantidad_combustible>20 and combustible()<=30:
        return ("dos")
    elif cantidad_combustible>30 and combustible()<=50:
        return ("tres")  
    else: 
        cantidad_combustible>50 
        return ("cuatro")
    
    
    


   
         
       
#evaluo mi variable distancia con mi funcion de peso
#Si queremos que la salida de un print() no provoque un cambio de línea y nos deje el cursor para que el siguiente print() continúe justo donde acabó el anterior, debemos facilitar el siguiente argumento: end=''
# print("distancia inicial: ",end="")
# print(distancia_inicial(distancia))
# print("El peso de la carga de toneladas:  ", end="")
# print(peso(distancia));
# print("la cantidad de combustible por gigalitros para el viaje es: ",end="")
# print(combustible())
# print("la cantidad de cohetes es:  ",end="")




print(distancia_inicial(distancia),"",peso(distancia),"",combustible())
print(CantidadCohetes())




