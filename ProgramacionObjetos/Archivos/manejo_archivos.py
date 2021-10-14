#Manejo de archivos 
try:
    #Se crea el archivo o se sobrescribe un archivo para escribir "w"
    #encoding="utf8 para soportar acentos
    archivo = open("C:\\Users\\yamit\\Documents\\Desarrollador_web\\Programacion_MisionTic\\Python\\Ejercicios\\ProgramacionObjetos\\Archivos\\prueba.txt","w",encoding="utf8")
    #Se escribe un archivo 
    archivo.write("Agregamos información al archivo\n")
    archivo.write("Adios\n")
    archivo.write("Ultima linea")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("Fin del archivo")