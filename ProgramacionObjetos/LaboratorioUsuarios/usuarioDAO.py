from conexion import Conexion
from usuario import Usuario
from logger_base import log

class UsuarioDAO:
    # DAO = Para esto, tenemos el patrón Arquitectónico Data Access Object (DAO), el cual permite separar la lógica de acceso a datos de los Objetos de negocios (Bussines Objects), de tal forma que el DAO encapsula toda la lógica de acceso de datos al resto de la aplicación.
    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                usuarios = []
                for registro in registros:
                    usuario = Usuario(registro[0],registro[1],registro[2])
                    usuarios.append(usuario)
                return usuarios    

    @classmethod
    def insertar(cls, usuario):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Usuario INSERTADO {usuario}")
                return cursor.rowcount
    
    @classmethod
    def actualizar(cls,usuario):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(usuario.username, usuario.password,usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR)
                log.debug(f"Usuario ACTUALIZADO: {usuario}")
                return cursor.rowcount
    
    @classmethod
    def eliminar(cls,usuario):
         with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(usuario.id_usuario)
                cursor.execute(cls._ELIMINAR)
                log.debug(f"Usuario ELIMINADO {usuario}")
                return cursor.rowcount


if __name__ == "__main__":
#INSERTAR
    usuario_1=Usuario(username="xiom",password=1098)
    usuarioInsertado_1=UsuarioDAO.insertar(usuario_1)
    log.debug(f"Usuario INSERTADAS: {usuarioInsertado_1}")

    usuario_2=Usuario(username="juanka",password=2022)
    usuarioInsertado_2=UsuarioDAO.insertar(usuario_2)
    log.debug(f"Usuario INSERTADAS: {usuarioInsertado_2}")

#ACTUALIZAR
    usuario_1=Usuario(7,"carlosuse",5566)
    usarioActualizado=UsuarioDAO.actualizar(usuario_1)
    log.debug(f"Usuario ACTUALIZADO {usarioActualizado}")


#SELECIONAR
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)