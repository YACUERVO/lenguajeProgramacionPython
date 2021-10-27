from logger_base import log
from psycopg2 import pool

class Conexion:
    #variables de clase
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "91021663366"
    _DB_PORT  = "5432"
    _HOST     = "127.0.0.1"
    _MIN_CON  = 1
    _MAX_CON  = 5
    _pool     = None #None para indicar que no se le quiere asignar a la variable nigun valor
                        

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                cls._MIN_CON,
                cls._MAX_CON,
                host=cls._HOST,
                user=cls._USERNAME,
                password=cls._PASSWORD,
                port=cls._DB_PORT,
                database=cls._DATABASE
                )
                log.debug(f"Creacion del POOL de conexion exitosa {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un erro al obtener el POOL de conexion {e}")
        else:
            return cls._pool

    #Funcion conexion
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexion obtenido del POOL: {conexion}")
        return conexion
    
    #Funcion liberar conexion del pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"Regresamos la conexion al POOL {conexion}")
    
    #Funcion Cerrar conexion
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
    
#Pruebas de la conexion

if __name__ == "__main__":
    conexion_1=Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_1)

    # conexion_2=Conexion.obtenerConexion()
    # Conexion.liberarConexion(conexion_2)

    # conexion_3=Conexion.obtenerConexion()
    # Conexion.liberarConexion(conexion_3)

