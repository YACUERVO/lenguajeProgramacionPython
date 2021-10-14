class MiClase:
    variable_clase="Valor variable clase"

    def __init__(self, variable_instancia):
        self._variable_intancia=variable_instancia

    #Metodos estaticos: No puede acceder a una variable de instancia
    @staticmethod
    def metodo_estatico():
        print("Metodo estatico".center(50,'-'))
        print(MiClase.variable_clase)
    
    #Metodo de clase: Se puede recibir informaciòn de si misma
    @classmethod
    def metodo_clase(cls):
        print("Metodo clase".center(50,'-'))
        print(cls.variable_clase)


print(MiClase.variable_clase)

objeto=MiClase("Valos variable instancia")

print(objeto._variable_intancia)
print(objeto.variable_clase)

#Objeto dos
objeto_1=MiClase("Objeto dos variable de clase")
print(objeto_1._variable_intancia)

#Llamando metodo estatio
MiClase.metodo_estatico()

#llamando metodo de clase
MiClase.metodo_clase()
