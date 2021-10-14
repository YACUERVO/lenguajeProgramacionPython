class Empleado:
    def __init__(self,nombre,sueldo):
        self._nombre=nombre
        self._sueldo=sueldo

    #Metodo de representación del objeto
    def __str__(self):
        return f"Nombre: {self._nombre} Sueldo: {self._sueldo}"
    
    def mostrar_detalles(self):
        return self.__str__


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self._departamento=departamento

    def __str__(self):
        return f"Departamento: {self._departamento} {super().__str__()}"


#para imprimir detalles del objeto aplicación del polimorfirmo 
#Metodo generico para realizar poimorfismo
def imprimir_detalle(objeto):   
    print(type(objeto))
    print(objeto)
    if isinstance(objeto,Gerente):
        print(objeto._departamento)
    # print(objeto.mostrar_detalles())



#Crear objetos 
empleado_1=Empleado("Yamith",250000)
imprimir_detalle(empleado_1)

gerente_1=Gerente("Laura", 350000, "Administrativo")
imprimir_detalle(gerente_1)