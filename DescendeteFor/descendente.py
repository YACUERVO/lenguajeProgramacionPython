#Numero decendentes con For

imprimir =int(input("Ingrese numero a imprimir decendentemente: "))



for contador in range(imprimir,0,-2):
    imprimir = imprimir-2 
    if imprimir % 2 == 0:               
        print(imprimir)
