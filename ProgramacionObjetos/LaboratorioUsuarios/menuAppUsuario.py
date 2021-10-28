from os import pipe
from logger_base import log
from usuarioDAO import UsuarioDAO
from usuario import Usuario

opcion = None

while opcion != 5:
    try:
        print("Iniciamos programa".center(50,'-'))
        print("Opciones")
        print("1. Listar usuarios")
        print("2. Agregar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = int(input("Escriba algunas de las opciones: 1 - 5: "))

        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        elif opcion == 2:
            username=input("Ingrese el username: ")
            password=input("Ingrese el password: ")
            usuario_1=Usuario(username=username,password=password)
            usuarioInsertar=UsuarioDAO.insertar(usuario_1)
            log.info(f"Usuario insertado {usuarioInsertar}")
        elif opcion == 3:
            id_usuario=int(input("Ingrese el campo actualizar: "))
            username=input("Ingrese el username: ")
            password=input("Ingrese el password: ")
            usuario_1=Usuario(id_usuario,username,password)
            usuarioActualizar = UsuarioDAO.actualizar(usuario_1)
            log.info(f"Usuario actualizado {usuarioActualizar}")
        elif opcion == 4:
            id_usuario=int(input("Ingrese el campo a eliminar: "))
            usuario_1=Usuario(id_usuario=id_usuario)
            usuarioEliminado=UsuarioDAO.eliminar(usuario_1)
            log.info(f"Usuario eliminado {usuarioEliminado}")
        else: 
            print("Salimos del programa".center(50,'-'))
            
    except Exception as e:
        log.error(f"Ocurrio un error {e}")
        opcion = None
 
        



