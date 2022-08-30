# usuario = input("usuario ")
# cantidad=int(input("monto a ingresar "))
# tiempo=int(input("tiempo del CDT"))



# #Funcion interes ganados 
# def valor(cantidad,tiempo):
#     valor=0
#     if tiempo<=2:
#         valor=cantidad * 0.02
#         valor=cantidad - valor
#     elif tiempo > 2:
#         valor=(cantidad * 0.03 * tiempo)/12
#         valor=valor + cantidad
#     return valor
    

# valor_total=valor(cantidad,tiempo)

# print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es:{valor_total}")

def CDT(usuario,cantidad,tiempo):
    valor=0
    if tiempo<=2:
        valor=cantidad * 0.02
        valor=cantidad - valor
    elif tiempo > 2:
        valor=(cantidad * 0.03 * tiempo)/12
        valor=valor + cantidad
    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valor}"


print(CDT("ASASD",10000000,3))