#Prodcuto de numeros pares de un conjunto de numeros

n= int(input())
a=[]
contador=0
while contador<n:
    numero = int(input())
    a.append(numero)
    contador+=1


producto = 0

for i in range(n):
    for j in range(i+1,n):
        producto = max(producto, a[i]*a[j])


print(producto)
