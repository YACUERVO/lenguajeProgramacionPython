class VolumenCubo:
    #iniciar atributos o variables
    def __init__(self, ancho, alto, profundidad):
        self.ancho=ancho
        self.alto=alto
        self.profundidad=profundidad

    #defino el metodo o funcion para calcular volumen
    def volumen(self):
        volumen=self.ancho*self.alto*self.profundidad
        return volumen


#Inicilizo las variables para que las ingrese el usuario
ancho_1=int(input("Ingrese ancho: "))
alto_1=int(input("Ingrese alto: "))
profundidad_1=int(input("Ingrese profundidad: "))

#crear objeto
VolumenCubo_1=VolumenCubo(ancho_1,alto_1,profundidad_1)

#llamar el metodo volumen
volumenTotal=VolumenCubo_1.volumen()

#imprimir el volumen en pantalla
print(f"El volumen es: {volumenTotal}")

