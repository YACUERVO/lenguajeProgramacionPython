class DispositivoEntrada:
    #Metodo inicializador
    def __init__(self, tipo_entrada, marca):
         
        self._tipo_entrada = tipo_entrada
        self._marca=marca

    #Metodos get:
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    @property
    def marca(self):
        return self._marca
    
    #Metodos set
    @tipo_entrada.setter
    def tipo_entrada(self,tipo_entrada):
        self._tipo_entrada = tipo_entrada
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    
    #Metodo imprimir
    def __str__(self):
        return f"Tipo de Entrada: {self._tipo_entrada} Marca: {self._marca}"


