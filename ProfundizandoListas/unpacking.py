# * operador para desempaquetar
numero=[1,2,3]
print(numero)
print(*numero)
print(*numero, sep='-')

#Para diccionarios doble **

#Desempaquetando al momento de pasar un parametro a una funcion
def suma(a,b,c):
    print(f"resultado {a+b+c}")

suma(*numero)

#Extraer algunas partes de una lista
mi_lista=[1,2,3,4,5,6]

a,*b,c,d=mi_lista
print(a,b,c,d)

#unir lista
lista1=[1,2,3]
lista2=[4,5,6]
lista3=[lista1,lista2]
print(f'lista de listas: {lista3}')
lista3=[*lista1,*lista2]
print(f'unir listas: {lista3}')

#Unir diccionarios
dic1={'A':1,'B':2,'C':3}
dic2={'D':4,'D':5,'D':6}
dic3={**dic1,**dic2}
print(f"Dicionario unido: {dic3}")

#Contruir una lista a partir un str
lista=[*'Hola mundo']
print(f"lista: {lista}")
print(*lista,sep='')