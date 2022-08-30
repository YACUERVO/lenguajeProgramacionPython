#Imprimir numero con FOR

# numero = 1

# for numero in range (101):
#     print(f"numero: {numero}")

#Ejercicio 1. Imprimir un rago de 0 a10 imprmier los divisibles entre 3
print("Numero divisibles entre 3")
for i in range (11):
    if i % 3 == 0:
        print(f"numero: {i}")

#Ejercicio 2. Crear un rango de numero de 2 a 6 e imprimirlos 
print("Numero entre 2 a 6")
for i in range (2,7):
    print(f"numero: {i}")

#Ejercicio 3. Crear un rango de numero de 3 a 10 pero con incremento de 2 a 10
print("Ingremento de 3 a 10 por 2")
for i in range(3,11,2):
    print(f"numero {i}")
