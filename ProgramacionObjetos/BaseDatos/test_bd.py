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

#Cursor es un objto para realizar sentencia de SQL desde python
cursor=conexion.cursor()

#Definir la sentencia que se quiere ejecutar en SQL
sentencia ="SELECT * FROM personas"

#Ejecutar la sentencia para llamar los registros
cursor.execute(sentencia)

#Recuperar los registros
registros = cursor.fetchall()
print(registros)

#Cerrar la base de datos
cursor.close()
conexion.close()