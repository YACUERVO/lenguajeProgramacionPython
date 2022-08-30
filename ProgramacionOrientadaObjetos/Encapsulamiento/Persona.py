class Persona:
    # El encapsulamiento es para no modificar los atributos
    def __init__(self,nombre,apellido,edad):
        self._nombre =nombre
        self._apellido =apellido
        self._edad =edad

    "Metodos get"
    @property
    def nombre(self):
        print("Llamando metodo get nombre")
        return self._nombre

    "Metodo set"
    @nombre.setter
    def nombre(self,nombre):
        print("Llamando metodo set nombre")
        self._nombre = nombre


    def mostrarDetalle(self):
        print (f"""
        mostrar detalle: 
            Nombre {self._nombre}
            Apellido {self._apellido}
            Edad {self._edad}                
                """)
    

           
            
          
persona =Persona("Yamith","Cuervo","30")  
persona.mostrarDetalle()


"Llamar el atributo de nombre a travez del metodo get"
# print(persona.nombre)
persona.nombre="Yamith Arley"
print(persona.nombre)