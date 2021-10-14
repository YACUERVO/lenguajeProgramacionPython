# Crear un programa en lenguaje de programación Python que reciba las coordenadas reales en X, Y y Z de dos vectores, y muestre el producto escalar entre ellos.


lista_x=[]
lista_y=[]
lista_z=[]
contador=0
tamaño_vector=int(input("Ingrese el tamaño de los vectores: "))

while contador<tamaño_vector:

    while True:
        x=((input("Ingrese vector X: ")))
        y=((input("Ingrese vector Y: ")))
        z=((input("Ingrese vector Z: ")))

        if x.isalpha() or y.isalpha() or z.isalpha() == True:
            print("Tiene que ingresar valores numericos")
        elif x.isdigit() and y.isdigit() and z.isdigit() ==True:
            break
        elif x.isalnum() or y.isalnum() or z.isalnum() == True:
            print("Ingresaste valores alfanumericos. Ingrese valores numericos")
    lista_x.append(x)
    lista_y.append(y)
    lista_z.append(z)
    
    contador=contador+1

#convertir los valores str en int
lista_x=[int(x) for x in lista_x] 
lista_y=[int(x) for x in lista_y]
lista_z=[int(x) for x in lista_z]
print(lista_x)
print(lista_y)
print(lista_z)


#multiplicamos item por item de cada lista 
producto_escalar=list(map(lambda x,y,z: x*y*z, lista_x,lista_y,lista_z))

print(producto_escalar)
    




