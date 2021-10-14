#Valor absoluto 
#Crear un programa en lenguaje de programación Python que reciba un número entero, y muestre como resultado su valor absoluto. Para los números positivos su valor absoluto es igual al mismo número (el valor absoluto de 35 es 35), mientras que para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -54 es 54).

numero = int(input("Ingrese el numero para convertirlo en valor Absoluto: "))

print(f"|{numero}|")

if numero >= 0:
    print(f"valor absoluto {numero}")
elif numero <= 0:
    numero = numero * -1
    print(f"valor absoluto {numero}")