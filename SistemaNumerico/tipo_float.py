#Profundizando tipo float

a=3.0
#Para indicar la cantidad de decimales que quiere que muestre
print(f"a: {a:.2f}" ) 

a=float(10)
print(f"a: {a:.2f}")

a=float('11')
print(f"a: {a:.2f}")

#Notacion exponencial (valores positivos o negativos)
a=3e5
print(f"a: {a}")

a=34e-5
print(f"a: {a}")

#Cualquier calculo que involucre un float, se promuece a float
a=4.0 + 5
print(f"suma: {a}")
print(type(a))