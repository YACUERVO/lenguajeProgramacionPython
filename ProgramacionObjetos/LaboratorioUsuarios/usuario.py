from logger_base import log


class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username    = username
        self._pasword     = password 
    def __str__(self):
        return f'''
            ID USUARIO: {self._id_usuario}
            USERNAME: {self._username}
            PASSWORD: {self._pasword}
        '''
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._pasword

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
    
    @username.setter
    def username(self,username):
        self._username = username
    
    @password.setter
    def password(self, password):
        self._pasword = password
    

if __name__ =="__main__":
    usuario_1=Usuario(1,"yacuervo",9102)
    log.debug(f"{usuario_1}" )

    usuario_2=Usuario(2,"milearenas",8205)
    log.debug(f"{usuario_2}")