import json


with open("files/data_file.json", "r") as read_file:
    data = json.loads(read_file.read())


print(data)
laminasFaltantes=str(input("Ingrese las laminas faltantes: "))

laminasFaltantes=laminasFaltantes.split()





precio=[]
precioTotal=0
for item in claves:
    for elemento_faltante in laminasFaltantes:  
        precio=data[item]
        if item == laminasFaltantes:
                precio+=precioTotal
                precio.append(laminasFaltantes)
            
      





    print(precio)

