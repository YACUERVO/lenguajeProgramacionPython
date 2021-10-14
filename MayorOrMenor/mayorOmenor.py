numero_1 = int(input("Proporciona el numero1: "))
numero_2= int(input("Proporciona el numero2: "))

if numero_1 > numero_2:
    print(f"el numero mayor es {numero_1}")
else:
    print(f"el numero mayor es {numero_2}")


libro=input("Nombre del libro: ")
ID=int(input("proporsiona el ID: "))
precio=float(input("Proporsiona el precio: "))
envio=(input("Indica si el envio es gratuito: "))

if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio="Valor incorrecto debe escribir true o false"

print(f'''
Nombre del libro es {libro}
Id: {id}
precio: {precio}
envio:{envio}
''')


valor = int(input("Proporcione un valor entre 0 y  10: "))

if 8 < valor < 9:
    print("A")
