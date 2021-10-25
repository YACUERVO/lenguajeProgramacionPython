from conexion import Conexion
from logger_base import log
from conexion_1 import Conexion
class CursorDelPool:
    def __init__(self):
        self._conexion=None
        self._cursor=None

    def __enter__(self):
        log.debug("Inicio del metodo with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor=self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exepcion, valor_excepcion, detalle_excepcion):
        log.debug("Se ejecuta metodo __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio una exepcion, se hace rollback: {valor_excepcion} {tipo_exepcion} {detalle_excepcion}")
        else:
            #Guardar los cambios en la base de datos
            self._conexion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
    
if __name__=="__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM personas")
        log.debug(cursor.fetchall())
