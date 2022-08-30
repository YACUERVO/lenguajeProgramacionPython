class Productos:
    contador=0

    
    #Iniciando los atributos de la clase productos
    def __init__(self,nombre,valor,cantidad,tipoProducto,fecha):
        Productos.contador+=1
        self._IdProducto=Productos.contador       
        self._nombre= nombre
        self._valor=valor
        self._cantidad=cantidad
        self._tipoProducto=tipoProducto
        self._fecha=fecha
   

    #Metodos de clase
    def __str__(self):
        return(f'''
        ID = {self._IdProducto}       
        Nombre: {self._nombre}
        Valor: {self._valor}
        Cantidad: {self._cantidad}
        Tipo de Producto: {self._tipoProducto}
        Fecha: {self._fecha}''')
    
    
      
    @property
    def valor(self):
        return self._valor

    @property
    def nombre(self):
        return self._nombre
    @property
    def tipoProducto(self):
        return self._tipoProducto
    @property
    def cantidad(self):
        return self._cantidad
    @property
    def valor(self):
        return self._valor
    @property
    def fecha(self):
        return self._fecha

     
  
  
  


if __name__ == "__main__":
    print('compras'.center(50,'-'))
    #Creando un objeto de la clase
    producto_1=Productos("Leche",1800,2,"canasta familiar","01/03/2022")

    producto_2=Productos("Pollo",3500,3,"basicos","04/03/2022")
  

    