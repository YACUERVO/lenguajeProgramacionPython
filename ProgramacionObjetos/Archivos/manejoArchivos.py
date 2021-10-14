
# #sintaxis diferente para abrir archivos con with
# with open("C:\\Users\\yamit\\Documents\\Desarrollador_web\\Programacion_MisionTic\\Python\\Ejercicios\\ProgramacionObjetos\\Archivos\\prueba.txt","r",encoding="utf8") as archivo:
from ManejoRecursos import ManejoRecursos




with ManejoRecursos("C:\\Users\\yamit\\Documents\\Desarrollador_web\\Programacion_MisionTic\\Python\\Ejercicios\\ProgramacionObjetos\\Archivos\\prueba.txt") as archivo:
    print(archivo.read())

    # abrir __enter__ 
    # cerrar __exit__