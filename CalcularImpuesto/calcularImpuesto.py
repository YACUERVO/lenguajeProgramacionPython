#Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.

valor=int(input("Ingrese valor: "))

def impuesto(valor):    
    valor*= 1.19 
    return valor

resultado=impuesto(valor)
 
print("el total de impuesto es", resultado)

pago=int(input("Ingrese valor a pagar: "))

def calcular_total(pago,impuesto):
    total=(pago*(impuesto/100))+pago
    return total

print("total a pagar:",calcular_total(pago,16))
