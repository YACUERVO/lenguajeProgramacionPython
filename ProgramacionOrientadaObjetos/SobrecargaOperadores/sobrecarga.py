#Sobrecarga de operadores
#De acuerdo a tipo de varibale se comportara distinto el operador suma
a= 2
b = 3

print(a+b)

a='Holas'
b="Mundos"
print(a + b)

a=[1,2,3,4]
b=[7,2,4,4]
print(a+b)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
         
    
    #Para agragar un objeto con otro onjeto para realizar el operador de suma
    def __add__(self,other):
        return f"{self.nombre} {other.nombre}"
    
    def __sub__(self,other):
        return self.edad - other.edad

       
persona = Persona("Yamith",30)
persona_1=Persona("Arley",25)
print(persona_1+persona)
print(persona - persona_1)

