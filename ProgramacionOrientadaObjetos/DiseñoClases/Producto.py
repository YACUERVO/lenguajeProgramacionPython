#Ejercicio de productos para ingresar en una orden de comprar
class Producto:
    #Variables de clases
    contador_producto = 0

    #Metodo Inicializador
    def __init__(self,nombre, precio):
        #Llamar la variable de clases por medio de la clase
        Producto.contador_producto += 1
        self._id_producto = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio
    
    #Metodo GET para retorna el valor 
    @property
    def precio(self):
        return self._precio

    
    def __str__(self):
        return f'''
        Id Producto {self._id_producto}
        Nombre {self._nombre}
        Precio {self._precio}
        '''
    
#Pruebas dentro del modulo producto
if __name__ == "__main__":
#Crear objetos de tipo producto
    producto_1 = Producto("Manzanas",1500)
    print(producto_1)

    producto_2 = Producto("Durazno",2000)
    print(producto_2)
    

