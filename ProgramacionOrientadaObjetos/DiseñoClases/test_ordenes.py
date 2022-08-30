from Producto import Producto
from Orden import Orden

#Objeto Productos 
producto_1 = Producto("Manzanas",1500)
producto_2 = Producto("Durazno",2000)
producto_3 = Producto("Naranjas",3000)
producto_4 = Producto("Pera",1800)

productoLista_1 = [producto_1, producto_2, producto_3]
productoLista_2=[producto_3,producto_4]

#Objeto Orden 
orden_1=Orden(productoLista_1)
orden_2=Orden(productoLista_2)
orden_1.agregar_producto(producto_3)
orden_2.agregar_producto(producto_1)

print(orden_1)
print("Total Orden 1", orden_1.calcular_total())
print(orden_2)
print("Total Orden 2", orden_2.calcular_total())

#Se crea objetos productos y crear objetos de tipo orden para asociar en el objeto  
