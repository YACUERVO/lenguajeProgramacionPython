try:    
    #Se abre un archivo para solo lectura con la letra "r"
    archivo = open("C:\\Users\\yamit\\Documents\\Desarrollador_web\\Programacion_MisionTic\\Python\\Ejercicios\\ProgramacionObjetos\\Archivos\\prueba.txt","r",encoding="utf8")
    #Leer el archivo
    #print(archivo.read())
    
    #leer algunos caracteres
    # print(archivo.read(5))

    # leer lineas completas
    # print(archivo.readline())
    # print(archivo.readline())

    #Interar el archivo cada una de las lineas
    # for linea in archivo:
    #     print(linea)

    #leer todas las lineas para agregarlo a una lista
    # print(archivo.readlines())

    #acceder a una linea del archivo por lienas
    # print(archivo.readlines()[2])

    #Copiar un archivo
    # a - anexar información 
    # w - sobreescribir información 
    archivo_2=open("C:\\Users\\yamit\\Documents\\Desarrollador_web\\Programacion_MisionTic\\Python\\Ejercicios\\ProgramacionObjetos\\Archivos\\copia.txt","a",encoding="utf8")
    archivo_2.write(archivo.read())


except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo_2.close()
    print("Fin del archivo")