from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    #variables de clase
    _DATABASE = "test_db"
    _USERNAME ="postgres"
    _PASSWORD ="91021663366"
    _DB_PORT ="5432"
    _HOST="127.0.0.1"
    _MIN_CON=1
    _MAX_CON=5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                host=cls._HOST,
                user=cls._USERNAME,
                password=cls._PASSWORD,
                port=cls._DB_PORT,
                database=cls._DATABASE             
                )
                log.debug(f"Creacion del pool exitosa {cls._pool}")
                return cls._pool                
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool {e}")
        else:
            return cls._pool  

    @classmethod
    #CLS atributos de clase
    def obtenerConexion(cls):
        conexion =cls.obtenerPool().getconn()
        log.debug(f"Conexion obtenido del pool: {conexion}")
        return conexion
    
    @classmethod
    #Liberar la conexion de pool
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)    
        log.debug(f"Regresamos la conexion al pool {conexion}")    

    @classmethod
    #Cerrar conexion
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
    

#Prueba
if __name__ == "__main__":
    conexion_1=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_1)

    conexion_2=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_2)

    conexion_3=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_3)

    conexion_4=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_4)

    conexion_5=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_5)