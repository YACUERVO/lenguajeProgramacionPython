
from Pelicula import Pelicula
from Servicio import Servicio


opcion = None

while opcion != 4:
    try:
        print("Opciones")
        print("1. Agregar Peliculas")
        print("2. Listar Peliculas")
        print("3. Eliminar catalogo de peliculas")
        print("4. Salir")
        opcion = int(input("Escribe tu opcion (1-4): "))
        if opcion == 1:
            nombre_pelicula = input("Propociona el nombre de la peliculas: ")
            pelicula=Pelicula(nombre_pelicula)
            Servicio.agregar_peliculas(pelicula)
        elif opcion == 2:
            Servicio.listar_metodo()
        elif opcion == 3:
            Servicio.eliminar_peliculas()        
    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None
else:
    print("Salimos del programa")
