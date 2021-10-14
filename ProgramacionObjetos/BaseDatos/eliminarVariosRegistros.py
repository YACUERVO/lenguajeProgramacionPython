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
            sentencia ="DELETE FROM personas WHERE id_persona IN %s"
            #sustituir los valores. Siemrpre la coma porque es uan tupla de valores
            entrada = input("Proposiona el id_persona a eliminar (separados por coma): ")
            valores=(tuple(entrada.split(',')),)
            
            cursor.execute(sentencia,valores)

            #Contar los registros
            registrosEliminados=cursor.rowcount
            print(f"Registros Eliminados: {registrosEliminados}")

        #Cerrar la base de datos
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:   
    conexion.close()
