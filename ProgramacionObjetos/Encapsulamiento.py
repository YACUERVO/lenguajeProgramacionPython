class Encapsulamiento:
    #definir los atributos 
    def __init__(self,nombre,apellido,edad):
        #el guion para que se no se acceda al atributo y que no se modifique 
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
    
    #medotos get = obtener y recuperar
    #@property decorador para optener el atributo de un metodo para qeu sea utlizado sin que sea un metodo 

    #metodos get para optener la información de los atributos
    @property 
    def nombre(self):        
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def edad(self):
        return self._edad
    
    
    #metodo set = colocar y modificar
    @nombre.setter
    def nombre(self, nombre):       
        self._nombre = nombre
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
    @edad.setter
    def edad(self,edad):
        self._edad=edad

    #metodo mostrar detalles
    def mostrar(self):       
        print(f"La persona {self._nombre} {self._apellido} {self._edad}")

    #metodo destructor para eliminar objetos
    def __del__(self):
        print(f"Perona: {self._nombre}, {self._apellido}")


if __name__=='__main__':#archivos de prueba
#crear objeto
    Encapsulamiento_1 = Encapsulamiento("Yamith", "Arley", 30)

#traer metodo get
#por el decorador @property se puee traer el atributo sin necesidad de traerlo como metodo

#traer metodo setter para modificar el objeto
    Encapsulamiento_1.apellido="cuervo"
    Encapsulamiento_1.edad="31"

    Encapsulamiento_1.mostrar()
    print(__name__)