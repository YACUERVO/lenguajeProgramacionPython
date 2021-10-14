import requests
import json

resultado = requests.get("https://www.datos.gov.co/resource/xdk5-pm3f.json")

# JSON -> Python
municipios = json.loads(resultado.text)

print("Sistema de municipios de Colombia")
print("Indique de cual departamento quiere ver los municipios:")
print("(1) Antioquia")
print("(2) Boyacá")
print("(3) Santander")
print("(4) Vichada")
print("(5) Cundinamarca")

# Validamos si el dato es correcto
while True:
  codigo_str = input("Ingrese el codigo: ")

  if codigo_str.isdigit() == False:
    print("Error: El texto ingresado NO es un número")

  elif len(codigo_str) != 1:
    print("Error: El número ingresado tiene MAS de un digito")

  else:
    codigo_int = int(codigo_str)

    if codigo_int < 1 or codigo_int > 5:
      print("Error: El codigo ingresado NO corresponde con ninguno de los departamentos")
    else:
      # Se superaron todas las validaciones
      break
  
# Mostramos el nombre de departamento seleccionado
# if codigo_int == 1:
#  print("\nA continuación se listan los municipios de Antioquia:\n")
# elif codigo_int == 2:
#  print("\nA continuación se listan los municipios de Boyacá:\n")
# elif codigo_int == 3:
#  print("\nA continuación se listan los municipios de Santander:\n")
# elif codigo_int == 4:
#  print("\nA continuación se listan los municipios de Vichada:\n")
# elif codigo_int == 5:
#  print("\nA continuación se listan los municipios de Cundinamarca:\n")

nombre_departamento_seleccionado = ""
if codigo_int == 1:
  nombre_departamento_seleccionado = "Antioquia"
elif codigo_int == 2:
  nombre_departamento_seleccionado = "Boyacá"
elif codigo_int == 3:
  nombre_departamento_seleccionado = "Santander"
elif codigo_int == 4:
  nombre_departamento_seleccionado = "Vichada"
elif codigo_int == 5:
  nombre_departamento_seleccionado = "Cundinamarca"

print(f"\nA continuación se listan los municipios de {nombre_departamento_seleccionado}:\n")

lista_municipios_por_mostrar = []

for municipio in municipios:

  departamento = municipio["departamento"].lower()
  nombre_municipio = municipio["municipio"]

  if codigo_int == 1 and departamento == "antioquia":
    lista_municipios_por_mostrar.append(nombre_municipio)

  elif codigo_int == 2 and departamento == "boyacá":
    lista_municipios_por_mostrar.append(nombre_municipio)

  elif codigo_int == 3 and departamento == "santander":
    lista_municipios_por_mostrar.append(nombre_municipio)

  elif codigo_int == 4 and departamento == "vichada":
    lista_municipios_por_mostrar.append(nombre_municipio)

  elif codigo_int == 5 and departamento == "cundinamarca":
    lista_municipios_por_mostrar.append(nombre_municipio)

lista_municipios_por_mostrar.sort()

for indice in range(len(lista_municipios_por_mostrar)):
  nombre_municipio = lista_municipios_por_mostrar[indice]
  print(f"#{indice}: {nombre_municipio}")

# https://www.datos.gov.co/resource/xdk5-pm3f.json