#Definimos nuestra funcion para sumar valores 

# *args: valores indefinidos


def sumerValores(*args):
    resultado=0
    for i in args:
        resultado+=i
    return resultado

def multiplar(*args):
    resultado=1 
    for i in args:
        resultado*=i 
    return resultado


#LLmada de la funcion 
print(sumerValores(3,5,9,5,5,7))
print(multiplar(2,2,2,3))
