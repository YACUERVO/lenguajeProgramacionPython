#Declarar variables
a,b="Hola","Adios"
print(a,b)

#swap(Intercambio1)
a,b=b,a
print(a,b)

#Regresar multiples valores en una funcion

def mimax(elementos):
    return min(elementos), max(elementos)

min, max=mimax([1,2,3,4,5])
print(f"minimo: {min}, maximo: {max}")

#regresar la suma de una tupla
resultado=sum((1,2,3,4,5))
print(f"Resultado: {resultado}")

def sumar(*args):
    return sum(args)

resultado=sumar(1,2,3,4,5)

print(f"resultdo suma: {resultado}")