# Crear un programa en lenguaje de programación Python que reciba una cantidad N de asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, Historia y Lenguaje) y las almacene en una lista, luego pida al usuario la nota que ha sacado un estudiante en cada asignatura (las notas son números decimales entre 0.0 a 5.0) y las almacene en otra lista. Luego el programa debe mostrar como resultado el nombre de las asignaturas que el usuario tiene que repetir (las que tengan menos de 3.0). El número N lo debe ingresar el usuario y debe ser validado (entero positivo, mayor o igual a 3).

from typing import Tuple


while True:
    cantidadAsignatura=input("Ingrese la cantidad de Asignaturas: ")

    if cantidadAsignatura.isalpha() == True:
        print("Ingreso un valor alfanumerico, dato incorrecto")
    elif cantidadAsignatura.isdigit() == True:
        break
    elif cantidadAsignatura.isalnum() == True:
        print("Ingreso un valor incorrecto alfanumerico")


contador = 0
asignatura=[]

while contador <= int(cantidadAsignatura):
    materia=input(f"Ingrese Materia {contador}: ")
    asignatura.append(materia)
    contador +=1
print(asignatura)

notas=[]
asignaturaClaves=dict.fromkeys(asignatura)
# print(asignaturaClaves)

for key,value in asignaturaClaves.items():
    nota =input(f"Ingrese la nota para {key} : ")    
    if value == None:
        asignaturaClaves[key] = nota

print(asignaturaClaves)


def repetir_materias():
    materiaRepetir=[]
    for key, value in asignaturaClaves.items():
        value = int(value) #convertir el valor del diccionario en un elemento entero para realizar la comparacion 
        if value <= 3:
            materiaRepetir.append(key)
    return materiaRepetir



print(f"Las materias a repetir son: ",','.join(repetir_materias()))
        


        




