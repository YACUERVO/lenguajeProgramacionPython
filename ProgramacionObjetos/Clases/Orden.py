
from Producto import Producto


class Orden:
    #Iniciar la variable 
    contador_ordenes=0

    def __init__(self,productos):
        Orden.contador_ordenes+=1
        self._IdOrden=Orden.contador_ordenes
        self._productos=list(productos)
    
    def agregar_producto(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
        
    def __str__(self):
        productos_str=''
        for producto in self._productos:
            productos_str+= producto.__str__()
        return f"Orden: {self._IdOrden}, Productos: {productos_str}"
    

if __name__ == "__main__":
    producto_1=Producto("Camisa", 1200)    
    producto_2=Producto("Pantalon", 1500)
    producto_lista_1=[producto_1,producto_2]
    orden_1=Orden(producto_lista_1)
    print(orden_1)
    orden_2=Orden(producto_lista_1)
    print(orden_2)

    print(f"Total de productos orden 1: {orden_1.calcular_total()}")
    print(f"Total de productos orden 2: {orden_2.calcular_total()}")
