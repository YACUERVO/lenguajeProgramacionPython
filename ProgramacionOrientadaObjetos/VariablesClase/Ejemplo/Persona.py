#Ejemplo de variables de clase
class Persona:      

    #Definir variable de clase
    contador_persona = 0

    #Crear un metodo de clase para acceder a la variable de clase 
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona +=1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        Persona.contador_persona += 1
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'''
        Persona {self.id_persona}
        Nombre {self.nombre}
        Edad {self.edad}
        '''


#Crear Objetos

persona_1=Persona("Yamith","30") #Objeto 1
print(persona_1)

persona_2=Persona("Karla","28") #Objeto 2 
print(persona_2)

#Acceder a la variable de clase
print("Valor de la variable de clase", Persona.contador_persona)