from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion =None
        self._cursor=None
    
    def __enter__(self):
        log.debug("Incio del metodo with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_exepcion, valor_exepcion,detalle_excepcion):
        log.debug("Se ejecuta metodo __exit__")
        if valor_exepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio una exepcion, se hace rollback {valor_exepcion} {tipo_exepcion} {detalle_excepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

#Prueba del cursor del pool
if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM usuarios")
        log.debug(cursor.fetchall())