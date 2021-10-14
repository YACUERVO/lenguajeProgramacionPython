nombreProducto = input("");
costoUnitario = int(input(""));
precioVenta=int(input(""))
cantidadDisponible = int(input(""))

def ganancia():
    totalGanancias = (precioVenta * cantidadDisponible) - (costoUnitario*cantidadDisponible);
    return totalGanancias
    





print("Producto:", nombreProducto)
print("CU:","$",costoUnitario)
print("PVP:","$",precioVenta)
print("Unidades Disponibles:", cantidadDisponible)
print("Ganancia:","$",ganancia())