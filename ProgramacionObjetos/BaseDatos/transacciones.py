import psycopg2 as bd


conexion = bd.connect(
    user = 'postgres',
    password='91021663366',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try: 
    #Iniciar la transaccion con autocommit
    conexion.autocommit=False
    #Obejto cursos para realizar comandos SQL
    cursor=conexion.cursor()
    setencia ="INSERT INTO personas(nombre,apellido,email) VALUES(%s,%s,%s)"
    #Valores a registrar en la base de datos
    valores=("Maria","Esperanzaz Gomez","esperanzagomez@gmail.com")

    #Ejecutar el objeto cursor para insertar los valores a la base de datos
    cursor.execute(setencia,valores)

    setencia="UPDATE personas SET nombre=%s,apellido=%s,email=%s WHERE id_persona= %s"
    valores=("Manuel","Chicamocha","manuel@gmail.com",14)
    cursor.execute(setencia,valores)

    #Commit para guardar la transaccion
    conexion.commit()
    print("Termina la transaccion")

    #Cerrar la base de datos
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, se hizo rollback {e}")
finally:   
    conexion.close()
