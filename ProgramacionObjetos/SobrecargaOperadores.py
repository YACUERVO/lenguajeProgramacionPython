class SobrecargaOperadores:
    #Operador de suma

    def __init__(self,nombre, edad):
        self._nombre=nombre
        self._edad=edad

    def __add__(self,otro):
        return f"{self._nombre} {otro._nombre}"
    
    def __sub__ (self,otro):
        return self._edad - otro._edad


persona_1=SobrecargaOperadores("Yamith",30)
persona_2=SobrecargaOperadores("Xiomara", 15)

#Metodo suma add o concatenar strings
print(persona_1.__add__(persona_2))
print(persona_1 + persona_2)

#Metodo resta sub
print(persona_1 - persona_2)
print(persona_1.__sub__(persona_2))


