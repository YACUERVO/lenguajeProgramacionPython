#triangulo impares de aceurdo a las columnas
#Crear un programa en lenguaje de programación Python que reciba un número entero positivo, y muestre un triángulo de números impares cuya cantidad de filas sea igual al número ingresado. El triángulo debe mostrar los números impares en cada fila, ordenados de mayor a menor desde la izquierda.


# Ej. Si el usuario ingresa el número 5, el programa debe mostrar lo siguiente:


# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1



columna = input("Ingrese la columna: ")

contador = 0

while contador<1:
    while True:
        if columna.isalpha():
            columna=input("ingresaste valores alfabeticas, ingresa valor numerico: ")

        elif int(columna) < 0:                       
            columna=input("Ingresaste numero negativo, ingrese numero positivo: ")    
                         
        elif int(columna) >0:
            print("ingresaste numero positivo")
            break
        

    contador+=1


# def impares():        
#     impares=10
    
#     while impares>contador:        
#         impares = impares-2
#         print(impares)
   


# ancho=impares()

columna=int(columna)
contador=0
impares = -1
m=""
while contador<columna:      
    cont =0    
    while cont<columna:
        impares = impares+2
        m=str(impares)+m       
        cont+=1
        print(m)
        contador+=1



 

                


        