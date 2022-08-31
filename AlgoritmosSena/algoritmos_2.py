#Habitualmente se entiende por palíndromo aquel que toma por unidad la letra, es decir, cuya última letra es la misma que la primera, la penúltima es la misma que la segunda, etc.
# Seres
# Sobreverbos
# Solos
# Sometemos
# Arañara
# Arenera.

#Creamos una variable

palabra=input("Ingrese la palabra: ")
#Creamos una condición 
if str(palabra) == "".join(reversed(palabra)):
    print("Es palindromo")
else:
    print("No es palindromo")

#Verificaremos el ejercicio
#Se realiza la verificación y el algoritmo valida los datos 