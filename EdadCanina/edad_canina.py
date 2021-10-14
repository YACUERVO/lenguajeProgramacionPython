#Edad canina 
#Crear un programa en lenguaje de programación Python que calcule el equivalente humano de la edad de un perro. Los dos primeros años de vida de un perro equivalen cada uno a diez y medio años humanos, y los siguientes años de vida de un perro equivalen cada uno a cuatro años humanos.

edad_perro= int(input("Ingrese la edad de su perro: "))

def edadPerro():
    if edad_perro <= 2: 
        return edad_perro*10.5
    elif edad_perro > 2:
        return (((edad_perro-2)*4) + (2*10.5))


print(f"la edad de su perro es:", edadPerro())
