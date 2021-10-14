#Importar la clases DispositivoEntrada
from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0
    #Metodo de inicializador de atributos
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contadorRatones += 1
        self._ID_raton = Raton.contadorRatones

    #Metodo para imprimir valores
    def __str__(self) -> str:
        return f"ID: {self._ID_raton} {super().__str__()}"

#Test para probar la clase raton creando un objeto
if __name__ == '__main__':
    raton_1=Raton("USB", "Accer")    
    print(raton_1)

    raton_2=Raton("USB", "Accer")    
    print(raton_2)
