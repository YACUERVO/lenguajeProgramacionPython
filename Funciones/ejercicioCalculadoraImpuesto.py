#Funcio que calcule el total de un pago incluyendo el impuesto 

def calcularTotalPago(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal

#Ejecutamos la funcion 
pagoSinImpuesto = float(input("Propocione el impuesto "))
impuesto = float(input("Porporciona el impuestoImpuesto "))

pagoConImpuesto=calcularTotalPago(pagoSinImpuesto,impuesto)
print(f"Pago con impuesto {pagoSinImpuesto}")
