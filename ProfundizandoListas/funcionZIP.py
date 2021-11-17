#Unir uno o mas interables

#print(dir(__builtins__))
#print(help(zip))
numeros=[1,2,3]
letras=['a','b','c']
identificadores= 321,322,323,324,325
mezcla=zip(numeros,letras,identificadores)
print(mezcla)
print(list(mezcla))
print(tuple(zip(numeros,letras)))

#Interar en paralelo
for numero, letras, identificadores in zip (numeros,letras,identificadores):
    print(f"Numero: {numeros}, letra: {letras}, identificadores: {identificadores}")

# nueva_lista=[]
# for numero, letras, identificadores in zip (numeros,letras,identificadores):
#     nueva_lista.append(f"{numero},{letras},{identificadores}")
# print(nueva_lista)



#Ordenamiento 
letras = ['c','d','a','e','b']
numero =[3,2,4,1,0]
mezcla=zip(letras,numero)
print(tuple(mezcla))

print(sorted(zip(letras,numero)))

#Crear Diccionario con zip y dos iterables
llaves=['Nombres','Apellido','Edad']
valores=['Juan','Perez','18']
diccionario=dict(zip(llaves,valores))
print(diccionario)

#Actualizar un elemento
llave=['Edad']
nuevaEdad=[28]
diccionario.update(zip(llaves,nuevaEdad))
print(diccionario)