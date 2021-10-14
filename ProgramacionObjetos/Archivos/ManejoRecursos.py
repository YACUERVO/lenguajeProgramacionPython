class ManejoRecursos:
    #para abrir una base de datos
    def __init__(self, nombre):
        self._nombre=nombre

    #abrir archivo
    def __enter__(self):
        print("Obtenemos el recurso".center(50,'-'))
        self._nombre= open(self._nombre, 'r', encoding='utf8')
        return self._nombre
    #cerrar archivo
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print("Cerramos el recurso".center(50,'-'))
        if self._nombre:
            self._nombre.close()
    

    
    
