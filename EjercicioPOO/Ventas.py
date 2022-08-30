#Importar clase producto
from Productos import Productos
from datetime import datetime

class Ventas:
    def __init__(self, productos):
        self._productos=list(productos)
    
    def valorCanastaFamiliar(self):    
        total = 0   
        devolucion = 0     
        for producto in self._productos:            
            if producto.tipoProducto == "canasta familiar":
                total += producto.cantidad * producto.valor 
        if total <= 250000:
            devolucion += total * 0.04
        return f'''
        Valor total Canasta familiar {total} 
        Devolucion Canasta familiar {devolucion}'''                

    def valorBasicos(self):
        total=0
        devolucion = 0  
        for producto in self._productos:
            if producto.tipoProducto == "basicos":
                total += (producto.cantidad * producto.valor) * 1.08  
        
        if total <= 380000:            
            devolucion += total * 0.03
        return f'''
        Valor total Basicos: {total}
        Devolucion Basicos: {devolucion}'''

    def valorNecesarios(self):
        total=0
        for producto in self._productos:
            if producto.tipoProducto == "necesarios":
                total += (producto.cantidad * producto.valor) * 1.12       
        return f'''
        Valor total Necesarios: {total}'''

    def valorLujo(self):
        total=0
        for producto in self._productos:
            if producto.tipoProducto == "lujos":
                total += (producto.cantidad * producto.valor) * 1.22         
        return f'''
        Valor total Lujos: {total}'''       
        
    def PromedioVenta(self):
        promedioCanasta  = 0
        promedioBasicos = 0
        promedioNecesarios= 0
        promedioLujo=0     
        fechaFinal = datetime.strptime( "31-03-2022","%d-%m-%Y")
        fechainicial = datetime.strptime( "31-03-2022","%d-%m-%Y")
        for producto in self._productos:
            if fechainicial >= datetime.strptime(producto.fecha,"%d-%m-%Y") and datetime.strptime(producto.fecha,"%d-%m-%Y")<= fechaFinal:
                if producto.tipoProducto == "canasta familiar":
                    promedioCanasta += producto.cantidad * producto.valor / producto.cantidad
                elif producto.tipoProducto == "basicos":
                    promedioBasicos += producto.cantidad * producto.valor / producto.cantidad
                elif producto.tipoProducto == "necesarios":
                    promedioNecesarios += producto.cantidad * producto.valor / producto.cantidad
                elif producto.tipoProducto == "lujos":
                    promedioLujo += producto.cantidad * producto.valor / producto.cantidad
                       
        return f'''
        promedio canasta {promedioCanasta}
        promedio baasicos {promedioBasicos} 
        promedio Necesarios {promedioNecesarios}
        promedio lujo {promedioLujo}'''
                

    def __str__(self):
        productos_str=''
        for producto in self._productos:
            productos_str+= producto.__str__()
        return f"Productos: {productos_str}"



if __name__ == "__main__":
    print('compras'.center(50,'-'))
    #Creando un objeto de la clase prodcutos
    producto_1=Productos("Leche",3800,5,"basicos","01-03-2022")    
    producto_2=Productos("Pollo",7500,3,"basicos","04-03-2022")   
    producto_3=Productos("Carne",10000,5,"canasta familiar","04-03-2022")
    producto_4=Productos("Jabon",4500,3,"necesarios","04-03-2022")
    producto_5=Productos("Papel",3500,1,"necesarios","04-03-2022")
    producto_6=Productos("Relog",22000,2,"lujos","04-03-2022")
    producto_7=Productos("Cadena",12500,1,"lujos","04-03-2022")

    #Creamos una lista con todos los productos
    lista=[producto_1,producto_2,producto_3,producto_4,producto_5,producto_6,producto_7]

    #Creamo un objeto de la clase Ventas
    ventas_1=Ventas(lista)

    #Imprimimos los productos
    print(ventas_1)

    #Metodos para calcular el valor de los prodcutos 
    print(ventas_1.valorCanastaFamiliar())
    print(ventas_1.valorBasicos())
    print(ventas_1.valorNecesarios())
    print(ventas_1.valorLujo())

    print(ventas_1.PromedioVenta())
