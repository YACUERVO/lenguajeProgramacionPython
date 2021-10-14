from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor


class Computadora:
    contadorComputadora=0

    #Metodo inicializador
    def __init__(self, nombre, monitor,teclado,raton):
        Computadora.contadorComputadora+=1
        self._ID_computadora = Computadora.contadorComputadora
        self._nombre = nombre
        self._monitor=monitor
        self._teclado = teclado
        self._raton = raton

    #Metodo para visualizar 
    def __str__(self):
        return f'''
        ID {self._ID_computadora} : {self._nombre}
        Monitor : {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}        
        '''

#Crear objetos de cada uno 
if __name__ == "__main__":
    #Objeto 1
    teclado_1 = Teclado("Usb","Accer")
    raton_1=Raton("Usb", "Apple")
    monitor_1=Monitor("HP","15")

    computadora_1 =Computadora("Apple", monitor_1,teclado_1,raton_1)
    print(computadora_1)

    #Objeto 2 
    teclado_2 = Teclado("Usb","Legion")
    raton_2=Raton("Usb", "Apple")
    monitor_2=Monitor("HP","14")

    computadora_2 =Computadora("Accer", monitor_2,teclado_2,raton_2)
    print(computadora_2)

    #Objeto 3 
    teclado_3 = Teclado("Usb","Hp")
    raton_3=Raton("Usb", "Apple")
    monitor_3=Monitor("HP","14")

    computadora_3 =Computadora("Hp", monitor_3,teclado_3,raton_3)
    print(computadora_3)