from Producto import Producto
from Orden import Orden



producto_1=Producto("Camisa", 1200)    
producto_2=Producto("Pantalon", 1500)
producto_3=Producto("Calcetines", 200)
producto_4=Producto("Blusa",1700)

producto_lista_1=[producto_1,producto_2]
producto_lista_2=[producto_3,producto_4]

orden_1=Orden(producto_lista_1)
orden_1.agregar_producto(producto_3)
orden_1.agregar_producto(producto_4)
print(orden_1)
print(f"Total de productos orden 1: {orden_1.calcular_total()}")

orden_2=Orden(producto_lista_2)
print(orden_2)
print(f"Total de productos orden 2: {orden_2.calcular_total()}")
