#Año Bisiesto 
#Crear un programa en lenguaje de programación Python que indique si un año es bisiesto o no. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400. Les comparto una pagina de Microsoft que describe como solucionar este problema en Excel, tal vez les sirva de guia...


año = int(input("Ingrese el año para validación: "))

def añoBisiesto():
    if  año % 4 == 0 and not(año%100==0) or año % 100 == 0 and año % 400 == 0:
        print ("año bisiesto")
    else:
        print("año no es bisiesto")
    


añoBisiesto()