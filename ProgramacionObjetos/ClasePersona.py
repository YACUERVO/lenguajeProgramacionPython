class ClasePersona:
    #caracteristicas y metodos para python
    #metodo inicializador init para iniciarlizar atributos
    def __init__(self):
        #Definimos atributos dentro de nuestro metodo init
        self.nombre='Yamith'
        self.apellido='Cuervo'
        self.edad='30'


#crea objeto
persona_1 = ClasePersona() #se crea objeto para poder acceder a los atributos de la clase
print(persona_1.nombre)
print(persona_1.apellido)
print(persona_1.edad)

