#Validar su una cadena esta incluida en la otra

texto_1=input("Ingrese Cadena de texto uno: ")
texto_2=input("Ingrese Cadena de texto dos: ")

texto_sub1=texto_1.replace(" ","")
texto_sub2=texto_2.replace(" ","")

# print(texto_1)

contador=0
while contador < 1:
    while True:
        if texto_sub1.isalpha() and texto_sub2.isalpha():
            print("Continue")
            break
        elif texto_sub1.isdigit() and texto_sub2.isdigit():
            texto_sub1=input("Ingrese nuevamente una cadena de texto 1:")
            texto_sub2=input("Ingrese nuevamente una cadena de texto 2:")
        elif texto_sub1.isdigit() and texto_sub2.isalpha():
            texto_sub1=input("Ingrese nuevamente una cadena de texto 1...:")
        elif texto_sub1.isalpha() and texto_sub2.isdigit():
            texto_sub2=input("Ingrese nuevamente una cadena de texto 2...:")
        elif len(texto_sub1)<0 and len(texto_sub2)<0:
            texto_sub1=input("Ingrese nuevamente una cadena de texto 1:")
            texto_sub2=input("Ingrese nuevamente una cadena de texto 2:")


    contador+=1


# print(texto_1)
# print(texto_2)
         
     
for x in texto_2:

    for y in texto_1[:]:   
        if x in y:
            print(f"el texto {texto_2} esta inlcuido {texto_1}")    
            break
       
       















