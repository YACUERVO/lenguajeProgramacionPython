from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDao:
    
    # DAO(Data access object)
    # CRUD (Create-read-update-delete)
    
    _SELECCIONAR = 'SELECT * FROM personas ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM personas WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

if __name__ == '__main__':
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)