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
                #Sentencia para realizar un resgitro en la base de datos
            sentencia ="UPDATE personas SET nombre=%s,apellido=%s,email=%s WHERE id_persona= %s"
            #sustituir los valores
            valores=("Juan Carlos","Perez Suarez","jcperez@gmail.com",7)
            
            cursor.execute(sentencia,valores)

            #Contar los registros
            registrosActualizados=cursor.rowcount
            print(f"Registros Actualizados: {registrosActualizados}")

        #Cerrar la base de datos
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:   
    conexion.close()
