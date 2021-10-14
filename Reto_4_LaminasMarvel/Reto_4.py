import json
#Laminas Marvel


#Recibir diccionario en formato JSON
x=input(" ")

data = json.loads(x)
# with open("files/data_file.json", "r") as read_file:
#     data = json.loads(read_file.read())
# print(data)

laminasFaltantes=str(input(" "))

laminasFaltantes=laminasFaltantes.split(" ")

claves=data.keys()
claves=list(claves)


precio=[]
coleccion_comprar=[]
for elemento_faltante in laminasFaltantes:
    for elementos_laminas in claves:    
        if elemento_faltante == elementos_laminas:            
            coleccion_comprar.append(elemento_faltante)
            x=data.get(elemento_faltante)
            precio.append(x)

suma = sum(precio)
print(suma)

coleccion_comprar=" ".join(coleccion_comprar)

print(coleccion_comprar)








# valores=data.values()
# print(valores)
# data_lista=data.items()
# print(data_lista)

# coleccion=[]
# for elemento_tupla in data_lista:
#     for elementoFaltante in laminasFaltantes:
#         if elemento_tupla == elementoFaltante:
#             coleccion.append(elementoFaltante)

# print(coleccion)



# for elemento_Marvel in data.keys():
#     print(elemento_Marvel)
   








