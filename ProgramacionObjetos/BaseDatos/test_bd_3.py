#Instalar la libreria psycopg2, para la conexion de BASE DE DATOS con postgreSQL
#Importar libreria psycopg2
import psycopg2


conexion = psycopg2.connect(
    user = 'postgres',
    password='91021663366',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try: 
    with conexion:
        #Cursor es un objto para realizar sentencia de SQL desde python
        with conexion.cursor() as cursor:

            #Definir la sentencia que se quiere ejecutar en SQL
                #Sentencia para llamar un solo registro de la base de datos
            sentencia ="SELECT * FROM personas WHERE id_persona IN %s"
            #llaves_primarias=((1,2,3),)
            entrada=(input("Proporciona los id\'s a buscar (separado por comas): "))
            llaves_primarias=(tuple(entrada.split(',')),)

            #Ejecutar la sentencia para llamar los registros
            cursor.execute(sentencia,llaves_primarias)

            #Recuperar un solo registro
            registro = cursor.fetchall()
            for registro in registro:
                print(registro)

            #Cerrar la base de datos
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:   
    conexion.close()
