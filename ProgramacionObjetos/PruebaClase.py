from Encapsulamiento import Encapsulamiento
#from Encapsulamiento import * => Importar todas las clases

#formato de texto para imprimir
print("Creacion de objetos".center(50,'-'))

if __name__ =='__main__':
    #Realizar el objeto 
    Encapsulamiento_1 = Encapsulamiento("Yamith","Cuervo","30")

    #Traer la funcion mostrar de la clase Encapsulamiento
    Encapsulamiento_1.mostrar()



    print(__name__)

print("Eliminacion de objetos".center(50,'-'))
del Encapsulamiento_1