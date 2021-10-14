class Metodos:

    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    #crear metodo. Selg para instanciar el metodo dentro de la clase
    #variable self se debe colocar para acceder a los atributos dentro de la clase
    def mostrarDetalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")


persona_1=Metodos("Yamith","Cuervo",30)
#obejto y metodo para llamar
persona_1.mostrarDetalle()
#asignar un atributo, solo al objeto de persona_1
persona_1.telefono="3104925227"
print(persona_1.telefono)

persona_2=Metodos("Xiomara","Gelves",30)
persona_2.mostrarDetalle()

#forma para llamar el metodo con clase, metodo y objeto. No es tan comun
persona_3=Metodos("Lady","Katherin",29)
Metodos.mostrarDetalle(persona_3)