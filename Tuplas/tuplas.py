tuplas = (13,1,8,3,2,5,8)
lista = list(tuplas)
lista_1=[]

for elemento in lista:
    if elemento < 5:
        lista_1.append(elemento)

print(lista_1)
