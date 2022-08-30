class Persona:
    # Iniciar los atributos de la clase
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    #Metodos de clase
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")


#Crear objeto
persona_1=Persona("Juan","Apellido","28")
persona_1.mostrar_detalle()

persona_2=Persona("Karla","Gomez","30")
persona_2.mostrar_detalle()

#Imprimimos el parametro nombre


#Utilizar metodos

