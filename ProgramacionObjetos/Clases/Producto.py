class Producto:
    
    contadorProductos=0

    def __init__(self, nombre, precio):
        Producto.contadorProductos +=1
        #Crear variable del contador
        self._IDProductos = Producto.contadorProductos
        self._nombre = nombre
        self._precio=precio
    

    def __str__(self):

        print(f"Producto {self._IDProductos}".center(50,'-'))
        return f'''
        ID: {self._IDProductos}
        Producto: {self._nombre}
        Precio: {self._precio}       
        '''

    @property
    def precio(self):
        return self._precio


#Pruebas
if __name__ == "__main__":
    producto_1=Producto("Camisa", 1200)
    print(producto_1)
    producto_2=Producto("Pantalon", 1500)
    print(producto_2)