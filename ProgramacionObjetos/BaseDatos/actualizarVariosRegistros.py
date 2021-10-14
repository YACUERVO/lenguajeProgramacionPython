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
            valores=(
                ("Carlos Cesar","Esmeldo Fasci","fasci@gmail.com",6),
                ("Blanca Cecilia","Rojas Perez","fasci@gmail.com",5),
                ("Lady Katherin","Valero","fasci@gmail.com",4),                
                
                )
            
            cursor.executemany(sentencia,valores)

            #Contar los registros
            registrosActualizados=cursor.rowcount
            print(f"Registros Actualizados: {registrosActualizados}")

            #Cerrar la base de datos
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:   
    conexion.close()
