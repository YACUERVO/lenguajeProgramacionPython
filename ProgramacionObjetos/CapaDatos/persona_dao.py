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
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:            
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor: 
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount
    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor: 
                valores =(persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor: 
                valores=(persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Objeto eliminado: {persona}")
                return cursor.rowcount



if __name__ == '__main__':
    # Insertar registro
    # persona1 = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    # personas_insertadas = PersonaDao.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # #Actualizar persona
    # persona_1 =Persona(48,"Yamith Arley","Cuervo Corredor","yamithcuervo@outlook.com")
    # personas_actualiadas=PersonaDao.actualizar(persona_1)
    # log.debug(f"persona actualizadas {personas_actualiadas}")

    #Eliminar registro
    persona_1=Persona(id_persona=51)
    persona_eliminadas=PersonaDao.eliminar(persona_1)
    log.debug(f"Personas eliminadas: {persona_eliminadas}")

    #Seleccion objetos
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)

    