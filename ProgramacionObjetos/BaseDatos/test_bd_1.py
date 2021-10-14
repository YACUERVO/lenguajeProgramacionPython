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
            sentencia ="SELECT * FROM personas"

            #Ejecutar la sentencia para llamar los registros
            cursor.execute(sentencia)

            #Recuperar todos los registros
            registros = cursor.fetchall()
            print(registros)

            #Cerrar la base de datos
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:   
    conexion.close()

