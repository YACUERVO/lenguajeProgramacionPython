nombre_1=['Ymaith', 'Juan','Pedro']
nombre_2='lara maria gonzalo ernesto'.split()

#Suma listas
print(f"Suma listas: {nombre_1+nombre_2}")

#Extender una lista con otra lista
nombre_1.extend(nombre_2)
print(f"Extender la lista 1 con la lista 2 {nombre_1} ")

#lista de numeros
numero_1=[10,40,15,4,20,90,4]

#Obtener el indice del primer elemento encontrado en una lista
#help(list.index)
print(f"indice 4: {numero_1.index(90)}")

#Invertir el orden de los elementos de una lista
numero_1.reverse()
print(f'lista invertida: {numero_1}')

#Ordenar los elementos de una lista
numero_1.sort()
print(f'lista ordenada ascendente: {numero_1}' )

#Orndenar de manera descendente una lista
numero_1.sort(reverse=True)
print(f"lista ordenada descendente {numero_1}")

#obtener el valor min y max de una lista
print(f"Valor minimo {min(numero_1)}")
print(f"Valor minimo {max(numero_1)}")

#copiar los elementos de una lista
copiar=numero_1.copy()
print(f"sin copiar {numero_1}")
print(f"Copiar las referencias : {copiar}")

print(f"Misma referencia en memoria: {numero_1 is copiar}")
print(f"mismo contenido de la lista: {numero_1 == copiar}")

#Podemos usar el constructo de la lista para copiar
copiar = list(numero_1)
print(f"sin copiar {numero_1}")
print(f"Copiar las referencias : {copiar}")

print(f"Misma referencia en memoria: {numero_1 is copiar}")
print(f"mismo contenido de la lista: {numero_1 == copiar}")

#slicing para copiar
copiar=numero_1[:]
print(f"sin copiar {numero_1}")
print(f"Copiar las referencias : {copiar}")

print(f"Misma referencia en memoria: {numero_1 is copiar}")
print(f"mismo contenido de la lista: {numero_1 == copiar}")

#Multiplicacion de lista

listaMultiplicacion = 5*[[2,5]]
print(listaMultiplicacion)
print(f"misma referencia: {listaMultiplicacion[0] is listaMultiplicacion[1]}")
print(f"misma contenido: {listaMultiplicacion[0] == listaMultiplicacion[1]}")
listaMultiplicacion[2].append(10)
print(listaMultiplicacion)

