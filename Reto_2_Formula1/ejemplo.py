print("Bienvenido al programa que te dice si un caracter ingresado es una vocal o no, por favor ingresa el caracter y luego dale Enter\n")

# Toda nuestra logica está contenido dentro de un ciclo while infinito, para que todo el tiempo el programa pida una caracter y nos diga si es una vocal o no
while True:

  texto_ingresado = input("Ingrese un caracter: ")

  # Aca contamos la cantidad de caracteres escritos por el usuario
  cantidad_caracteres = len(texto_ingresado)

  # Si la cantidad de caracteres es DIFERENTE a 1, dejamos al usuario atrapado en un ciclo while hasta que escriba un texto con SOLO UNA LETRA
  while cantidad_caracteres != 1:
    
    # Mostramos mensajes informativos diferentes al usuario, dependiendo si NO escribió nada, o si lo que escribió tienen 2 o mas caractereres
    if cantidad_caracteres == 0:
      print("No escribió nada!\n")
    elif cantidad_caracteres >= 2:
      print(f"Escribió {cantidad_caracteres} caracteres! Solo es necesario uno!\n")

    texto_ingresado = input("Ingrese 1 caracter (OJO! solo uno!): ")

    # Aca contamos la cantidad de caracteres escritos por el usuario
    cantidad_caracteres = len(texto_ingresado)


  # En este punto del programa, tenemos total certeza de que el texto ingresado solo tiene UN CARACTER

  vocales = "aeiouAEIOU"

  # Aplicamos varios filtros de manera consecutiva para determinar la naturaleza del caracter ingresado:
  #   Si es una letra isalpha()
  #     Si es una vocal
  #     Si es una consonante
  #   Si es un digito numerico isdigit()
  #   Si es un caracter especial
  if texto_ingresado.isalpha():
    # Preguntamos cuantas veces se encuentra el caracter ingresada por el usuario dentro de la cadena de texto llamada 'vocales', la cual contiene todas las vocales (tanto mayusculas como minusculas)
    caracter_es_vocal = vocales.count(texto_ingresado)
  
    if caracter_es_vocal == 1:
      print(f"El caracter {texto_ingresado} es una VOCAL\n")
    else:
      print(f"El caracter {texto_ingresado} es una CONSONANTE\n")

  elif texto_ingresado.isdigit():
    print(f"El caracter {texto_ingresado} es un DIGITO NUMERICO\n")

  else:
    print(f"El caracter {texto_ingresado} es un CARACTER ESPECIAL\n")
