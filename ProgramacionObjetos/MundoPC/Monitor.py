class Monitor:
    contadorMonitores = 0

    #Metodo iniciando variables
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores +=1
        self._ID_monitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    #Metodo mostrar objeto
    def __str__(self):
        return f"ID: {self._ID_monitor} Marca: {self._marca} Tamaño: {self._tamaño}"


if __name__ == '__main__':
    monitor_1=Monitor("Apple", 15)    
    print(monitor_1)

    monitor_2=Monitor("Accer", 14)    
    print(monitor_2)