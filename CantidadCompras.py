import random 

class CantidadCompras:
    #Variables

    def __init__(self,cantidadTotal):        
        self._cantidadTotal=cantidadTotal

    @property
    def cantidadTotal(self):
        return self._cantidadTotal
    
    @cantidadTotal.setter
    def cantidadTotal(self,cantidadTotal):
        self._cantidadTotal =cantidadTotal
    
    #Metodo Mostrar detalles
    def __str__(self):
        return f"cantidad total: {self._cantidadTotal}"
  
    def validarDatos(self):  
        while True:            
            if self._cantidadTotal.isdigit()==True:
                break
            elif self._cantidadTotal.isalpha()==True:
                    print("Ingrese un numero entero: ")
                    self._cantidadTotal=input("Ingrese cantidad total de compras: ")
    
    def validarNumero(self):        
        total = 0
        if int(self._cantidadTotal) < 100:
            return "No aplica promocion"            
        else:
            print(f"Su gasto es superior a {self._cantidadTotal} participa en la promocion")
            numero = random.randint(1,5)            
            if numero == 1:
                return "No participa"                
            elif numero == 2:
                print("Aleatoriamente obtuvo una Bola Roja descuento 10%")
                total = int(self._cantidadTotal)-((int(self._cantidadTotal) * 0.1))
                return f"Su total a pagar es {total}"
            elif numero == 3:
                print("Aleatoriamente obtuvo una Bola Azul descuento 20%")
                total = int(self._cantidadTotal) - ((int(self._cantidadTotal) * 0.2))
                return f"Su total a pagar es {total}"
            elif numero == 4:
                print("Aleatoriamente obtuvo una Bola Verde descuento 25%")
                total = int(self._cantidadTotal) - ((int(self._cantidadTotal) * 0.25))
                return f"Su total a pagar es {total}"
            elif numero == 5:
                print("Aleatoriamente obtuvo una Bola Amarilla descuento 50%")
                total = int(self._cantidadTotal)- ((int(self._cantidadTotal) * 0.50))
                return f"Su total a pagar es {total}"

     

    
print("Vamos a Jugar".center(50,'-'))

#Crear objeto
cantidad=CantidadCompras(input("Ingrese la cantidad de compras: "))

#Metodo validar datos
cantidad.validarDatos()

#Metodo validar numero para promocion e imprimir
total=cantidad.validarNumero()
print(total)

#llamar metodo validar cantidad
# print(cantidad)
print("Game over".center(50,'-'))