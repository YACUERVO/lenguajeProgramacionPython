#Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

grados=int(input("Ingrese el valor de la temperatura Celsius: "))

grados_1=int(input("Ingrese el valor de la temperatura farenheit: "))

def celsius(gradosCelsius):
    return (gradosCelsius * 9.5)+32

def fahrenheit(gradosFahrenheit):
    return (gradosFahrenheit-32)/5.9


print("Los grados Celsius a fahrenheit: ", celsius(grados))
print("Los grados fahrenheit a Celsius: ", fahrenheit(grados_1))