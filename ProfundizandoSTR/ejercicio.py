#Leer contenido online

from urllib.request import urlopen

#abri recurso 
palabras=[]
with urlopen('http//globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    #Decodificar
    contenido = mensaje.read().decode('UTF-8')
    print(contenido)
    for linea in mensaje:
        palabras=linea.decode('utf-8').split()
        for palabra in palabras:
            #print(palabras)
            palabras.append(palabra)

# with open('nuevo_Archivo.txt','w',encoding='utf-8') as archivos:
#     archivos.write(contenido)
#contar ocurrencia de una cadena

print(contenido.count("univerisad"))