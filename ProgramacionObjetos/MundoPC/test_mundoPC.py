from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

 #Objeto 1
teclado_1 = Teclado("Usb","Accer")
raton_1=Raton("Usb", "Apple")
monitor_1=Monitor("HP","15")

computadora_1 =Computadora("Apple", monitor_1,teclado_1,raton_1)


#Objeto 2 
teclado_2 = Teclado("Usb","Legion")
raton_2=Raton("Usb", "Apple")
monitor_2=Monitor("HP","14")

computadora_2 =Computadora("Accer", monitor_2,teclado_2,raton_2)


#Objeto 3  
teclado_3 = Teclado("Usb","Hp")
raton_3=Raton("Usb", "Apple")
monitor_3=Monitor("HP","14")

computadora_3 =Computadora("Hp", monitor_3,teclado_3,raton_3)


#Crear lista para ingresar a la orden 
computadora_lista_1=[computadora_1,computadora_2]
computadora_lista_2=[computadora_2,computadora_3]

#Objeto Orden pasamos la lista
orden_1=Orden(computadora_lista_1)
print(orden_1)

orden_2=Orden(computadora_lista_2)
print(orden_2)

#Metodo agregar computadora
#Crear los objetos 
teclado_4=Teclado("Bluetooth","Gamer")
raton_4=Raton("Bluetooth", "Gamer-Legion")
monitor_4=Monitor("Gamer_Lenovo",17)
computadora_4=Computadora("Gamer",monitor_4,teclado_4,raton_4)


orden_1.agregar_computadoras(computadora_4)
print(orden_1)