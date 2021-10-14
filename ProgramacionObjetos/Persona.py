class Persona:
#las clases se definen las caracteristicas
    def __init__(self,nombre,apellido,edad):
        #la variable self es un atributo y a lado derecho estan los parametros. Clase verla como una plantilla
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

#constructor para inicializar un obejeto, y poder utilziar los atributos de la clase
persona_1=Persona("yamith","arley",30)
print(persona_1.nombre)
print(persona_1.apellido)
print(persona_1.edad)
print(f"objeto persona 1: {persona_1.nombre} {persona_1.apellido}")
#modificar parametros de los atributos
persona_1.nombre='Yamith Arley'
persona_1.apellido='Cuervo Corredor'
print(f"objeto persona 1: {persona_1.nombre} {persona_1.apellido}")


persona_2=Persona("xiomara","gelvez",30)
print(persona_2.nombre)
print(persona_2.apellido)
print(persona_2.edad)
print(f"objeto persona 2: {persona_2.nombre} {persona_2.apellido}")

