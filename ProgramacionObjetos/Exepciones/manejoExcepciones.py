#Capturar el error en una variable
from ExepcionesPersonalizadas import NumerosIdenticosException

try:
    10/0
except Exception as e:
    print(f"Ocurrio un error:  {e}")


#Clases de excepcion:
    #Exception #Clase padre de mayor jerarquia
    #ZeroDivisionError #Clases hijas de menor jerarquia
    #TypeError #Clase hijas menor jerarquia
#Variable Para indica que no tiene ningun resultado, tipo de erro por variables    
resultado = None

try:
    a= int(input("Primer numero: "))
    b = int(input("Segundo Numero: "))
    if a==b:
        raise NumerosIdenticosException("Numeros identicos")
        #raise se utliza para exepciones personalizadas

    resultado = a / b
except TypeError as e:
    print(f"Ocurrio un de tipo TypError: {e}, {type(e)}")
except ZeroDivisionError as e:
    print(f"Ocurrio un tipo erro ZeroDivisionError: {e}, {type(e)}")
except ValueError as e:
    print(f"Ocurrio un tipo de erro ValueError: {e}, {type(e)}")
except Exception as e:
    print(f"Ocurrio un error Exception: {e}, {type(e)}")
else:
    print("No se arrojo ninguna excepcion")
finally:#Siempre se ejecuta el bloque finally
    print("Ejecucion del bloque finally")


print(f"resultado: {resultado}")
print("continuamos...")

