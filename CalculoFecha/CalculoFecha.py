#Calculo de fecha
#Crear un programa en lenguaje de programación Python que reciba un número entero positivo entre 1 y 365, y calcule a que día y mes del presente año corresponde. Ej: El dia 100 corresponde al 10 de Abril de 2021. Si el número ingresado no pertenece al rango indicado antes, se le debe avisar al usuario que el número es inválido.



dia=int(input("Ingrese el día a calcular: "))



def calculo_mes():    
    if dia <= 30:
        return ("Enero del 2021")
    elif dia > 30 and dia <60:
        return ("Febrero del 2021")    
    elif dia > 60 and dia <= 90:
        return ("Marzo del 2021")
    elif dia > 90 and dia <= 120:
        return ("Abril del 2021")
    elif dia > 120 and dia <= 150:
        return ("Mayo del 2021")
    elif dia > 150 and dia <= 180:
        return ("Junio del 2021")
    elif dia > 180 and dia <= 210:
        return ("Julio del 2021")
    elif dia > 210 and dia <= 240:
        return ("Agosto del 2021")
    elif dia > 240 and dia <= 270:        
        return ("Septiembre del 2021")
    elif dia > 270 and dia <= 300:
        return ("Octubre del 2021")
    elif dia > 300 and dia <= 330:
        return ("Nombiembre del 2021")
    elif dia > 330 and dia <= 361:
        return ("Diciembre del 2021")        
    else:
        return ("dia no valido")


x = calculo_mes()

def calculo_dia():
    dia1 = dia % 30  
    return dia1

y = calculo_dia()

print(f"el día es {y} del mes {x}")

