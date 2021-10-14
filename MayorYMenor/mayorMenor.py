#Crear un programa en lenguaje de programación Python que reciba un número N (entero positivo, mayor o igual a 5), cree una lista de tamaño N, pida al usuario cada uno de los elementos a almacenar en la lista (números decimales y enteros, positivos, negativos y el cero), y luego muestre el número mayor y menor de la lista, asi como los indices de dichos elementos.


while True:
    tamañoLista=input("Tamaño de la lista:")
    
    if tamañoLista.isdigit() == True:          
        if int(tamañoLista) > 5:
            print("Ingresaste una lista mayor a 5")
        else:            
            break 
    elif tamañoLista.isalpha() == True:
        print("Ingresaste un valor alfabetico")
    elif tamañoLista.isalnum() == True:
        print("Ingresaste un valor alfanumerico")    
    elif int(tamañoLista)<0:
        print("Ingresaste un numero negativo")


lista=[]
contador=0


while contador < int(tamañoLista):
    elemento=int(input("Ingrese valor para la lista: "))
    lista.append(elemento)
    contador+=1

lista = sorted(lista)

print(lista)


nuevaLista=dict(zip(range(len(lista)), lista))

print(nuevaLista)
