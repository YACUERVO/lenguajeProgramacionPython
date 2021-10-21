import logging as log
#El registro es un medio de seguimiento de los eventos que ocurren cuando algunos software se ejecuta. El registro es importante para el desarrollo de software, depurar y ejecutar. Si usted no tiene ningún registro de registro y el programa se bloquea, hay muy pocas probabilidades de detectar la causa del problema.


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', 
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()                
                ])                    
                    

if __name__=="__main__":
    log.debug('Mensaje a nievl debug')
    log.info("Mensaje a nivel info")
    log.warning("Mensaje a nivel de warning")
    log.error("Mensaje a nivel de error ")
    log.critical("Mensaje a nivel critico")