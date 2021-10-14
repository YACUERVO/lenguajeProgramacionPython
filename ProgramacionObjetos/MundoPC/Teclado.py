from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    #Variable Global
    contadorTeclado=0
    #Metodo de iniciar variables
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contadorTeclado +=1
        self._ID_teclado=Teclado.contadorTeclado

    #Metodo para mostrar variables
    def __str__(self):
        return f"ID: {self._ID_teclado} {super().__str__()}"

#Test para probar la clase raton creando un objeto
if __name__ == '__main__':
    teclado_1=Teclado("USB", "HP")    
    print(teclado_1)

    teclado_2=Teclado("USB", "HP")    
    print(teclado_2)


    