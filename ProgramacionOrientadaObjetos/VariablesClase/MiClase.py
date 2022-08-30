class Miclase:
    
    variableClase = "Valor variable clase"

    def __init__(self,variableInstancia):
        self._variableInstancia = variableInstancia

    @staticmethod
    def metodoEstatico():
        return "Metodo de estatico"

    @classmethod
    def metodoClase(cls):
        print("Accediendo al metodo de clase")
        print(cls.variableClase)

    def metodo_instancia(self):
        self.metodoClase()
        self.metodoEstatico()
        print(self._variableInstancia)
        print(self.variableClase)



#Para acceder a la variable de clase debemos llamarla con la clase 
print(Miclase.variableClase)

#Para acceder a la varible de instancia debemos realizar un objeto 
miclase=Miclase("valor variable de instancia")
print(miclase._variableInstancia)
print(miclase.variableClase)

Miclase.variableClase_2="Valor variable clase 2"

miclase_2=Miclase("Otro valor de variable de instancia")
print(miclase_2._variableInstancia)
print(Miclase.variableClase_2)
print(miclase.variableClase_2)

x=Miclase.metodoEstatico()
print(x)

#Llamando el metodo de clase 
Miclase.metodoClase()

miObjeto_1=Miclase("VariableInstacia")
miObjeto_1.metodoClase()


print("Metodo de instancia")
miObjeto_1.metodo_instancia()

