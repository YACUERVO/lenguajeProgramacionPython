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
    @property
    def apellido(self):
        return self._apellido
    @property
    def edad(self):
        return self._edad
      

    "Metodo set"
    @nombre.setter
    def nombre(self,nombre):
        print("Llamando metodo set nombre")
        self._nombre = nombre
    @apellido.setter
    def apellido(self,apellido):
        self._apellido =apellido
    @edad.setter
    def edad(self,edad):
        self._edad =edad


    def mostrarDetalle(self):
        print (f"""
        mostrar detalle: 
            Nombre {self._nombre}
            Apellido {self._apellido}
            Edad {self._edad}                
                """)
    

         
if __name__ == "__main__":          
          
    persona =Persona("Yamith","Cuervo","30")  
    # persona.mostrarDetalle()
    print(f"Primer impresión sin modificar {persona.mostrarDetalle()}")

    "Llamar el atributo de nombre a travez del metodo get"
    # print(persona.nombre)
    persona.nombre="Yamith Arley"
    persona.apellido = "Corredor"
    persona.edad="32"
    persona.mostrarDetalle()
    print(f"Segunda impresión sin modificar {persona.mostrarDetalle()}")


