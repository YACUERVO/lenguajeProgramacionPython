class Orden:
    contadorOrdenes=0
    
    def __init__(self,computadoras):
        Orden.contadorOrdenes += 1
        self._ID_orden=Orden.contadorOrdenes
        self._computadora=list(computadoras)


    def agregar_computadoras(self, computadoras):
        self._computadora.append(computadoras)

    def __str__(self):
        computadora_str = ''
        for computadora in self._computadora:
            computadora_str += computadora.__str__()
        
        return f'''
        Orden : {self._ID_orden}
        Computadoras: {computadora_str}       
        
        '''