#matrices en python
matriz=[[10,20],[30,40,50],[60,70,80,90]]
print(f'Matriz: {matriz}')
print(f"fila 0, columna 0: {matriz[0][0]}")
print(f"fila 2, columna 2: {matriz[2][2]}")
matriz[2][0]=65
print(f"matriz modificada: {matriz}")

listasListas=[[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
listasListas.sort(key=len)
print(f"ordenar lista {listasListas}")

#sorted built-in 
nombres_1=['juan', 'karla','pedro','esperanza']
nombres_1=sorted(nombres_1)
print(nombres_1)

#ordenar de manera descendente
nombres_1=sorted(nombres_1,reverse=True)
print(nombres_1)

#ordenar por la cantidad de caracteres
nombres_1=sorted(nombres_1,key=len)
print(nombres_1)

#built-in reversed
nombres_1=reversed(nombres_1)
print(list(nombres_1))