
from datetime import datetime

contador =0

while contador <1:

    codigo=input("Ingrese codigo del producto: ")
    nombre=input("Ingrese nombre del producto: ")
    valor=int(input("Ingrese valor del producto: "))
    cantidad=int(input("Ingrese la cantidad: "))
    print('''
    Escriba el tipo de producto segun las opciones: 
    Canasta familiar = producto 1
    Basicos = producto 2
    Necesarios = producto 3
    Lujos = productos 4
    ''')
    tipoProducto = input("Ingrese tipo de producto: ")
    fecha=input("Ingrese Fecha: ")
    fecha = datetime.strptime(fecha,"%d-%m-%Y")

    def valorCanastaFamiliar(cantidad,valor):    
        total = 0   
        devolucion = 0     
        if tipoProducto == "producto 1":        
            total += cantidad * valor
        if total <= 250000:
            devolucion += total * 0.04
        return f'''
        Valor total Canasta familiar {total} 
        Devolucion Canasta familiar {devolucion}'''                

    def valorBasicos(cantidad,valor):
        total=0
        devolucion = 0      
        if tipoProducto == "producto 2":
            total += (cantidad * valor)* 1.08          
        if total <= 380000:            
            devolucion += total * 0.03
        return f'''
        Valor total Basicos: {total}
        Devolucion Basicos: {devolucion}'''

    def valorNecesarios(cantidad, valor):
        total=0        
        if tipoProducto == "producto 3":
            total += (cantidad * valor) * 1.12       
        return f'''
        Valor total Necesarios: {total}'''

    def valorLujo(cantidad,valor):
        total=0        
        if tipoProducto == "producto 4":
            total += (cantidad *valor) * 1.22         
        return f'''
        Valor total Lujos: {total}'''      

    def PromedioVenta(cantidad,valor,fecha):
        promedio = 0  
        fechaFinal = datetime.strptime( "31-03-2022","%d-%m-%Y")
        fechainicial = datetime.strptime( "31-03-2022","%d-%m-%Y")  
        if fechainicial >=  fecha and fecha <= fechaFinal:
            promedio += cantidad * valor / cantidad
            print (f"Promedio de ventas: {promedio}")   
        else:
            print("Fecha no corresponde al periodo de marzo")       
    
    contador += 1
                       
   


print(valorCanastaFamiliar(cantidad,valor))
print(valorBasicos(cantidad,valor))
print(valorNecesarios(cantidad,valor))
print(valorLujo(cantidad,valor))
PromedioVenta(cantidad,valor,fecha)