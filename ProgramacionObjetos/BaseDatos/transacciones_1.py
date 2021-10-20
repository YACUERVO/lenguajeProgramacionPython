import psycopg2 as bd
#Manejo de recursos para realizar transacciones

conexion = bd.connect(
    user = 'postgres',
    password='91021663366',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try: 
    #Iniciar la transaccion con with
    with conexion:
        with conexion.cursor() as cursor:
            #Obejto cursos para realizar comandos SQL        
            setencia ="INSERT INTO personas(nombre,apellido,email) VALUES(%s,%s,%s)"
            #Valores a registrar en la base de datos
            valores=("Laura","Echeverria","laura@gmail.com")

            #Ejecutar el objeto cursor para insertar los valores a la base de datos
            cursor.execute(setencia,valores)

            setencia="UPDATE personas SET nombre=%s,apellido=%s,email=%s WHERE id_persona= %s"
            valores=("Manuel","Chicamocha","manuel@gmail.com",)
            cursor.execute(setencia,valores) 
        

    #Cerrar la base de datos
except Exception as e:    
    print(f"Ocurrio un error, se hizo rollback {e}")
finally:   
    conexion.close()
    
print("Termina la transaccion")