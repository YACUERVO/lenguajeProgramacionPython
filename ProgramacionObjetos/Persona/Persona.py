class Persona:
    contador_personas=0

    #Crear un metodo clase para realizar un contador
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas+=1
        return cls.contador_personas

    
    def __init__(self,nombre,edad):
        Persona.contador_personas+=1
        self.id_persona = Persona.generar_siguiente_valor()
        self._nombre=nombre
        self._edad=edad

    def __str__(self):
        return f"Persona: ID {self.id_persona} Nombre: {self._nombre} Edad:{self._edad} "


Persona_1=Persona("Yamith", 30)
print(Persona_1)
Persona_2=Persona("Xiomara",30)
print(Persona_2)