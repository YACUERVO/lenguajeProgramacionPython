from Producto import Producto
class Orden:
    #Variable de clase
    contador_orden=0

    def __init__(self,producto):
    #Llamar la variable de clase
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._producto = list(producto)
    
    #Metodo de agragacion a la orden 
    def agregar_producto(self,producto):
        self._producto.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._producto:
            total += producto.precio
        return total

    def __str__(self):
        producto_str_=" "
        for producto in self._producto:
            producto_str_ += producto.__str__() + "------------------"
        return f'''
        Orden : {self._id_orden} 
        ------------------
        Producto : {producto_str_}'''

if __name__ == "__main__":
    producto_1 = Producto("Manzanas",1500)
    producto_2 = Producto("Durazno",2000)
    producto_3 = Producto("Naranjas",3000)
    productoLista_1 = [producto_1, producto_2, producto_3]
    orden_1=Orden(productoLista_1)
    print(orden_1)
