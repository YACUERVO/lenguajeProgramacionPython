MI_CONSTANTE = 'Valor de mi constante' #Se acustumbra que la constante en otro modulo 



class Matematicas:
    
    PI = 3.1416 #Variable de clase



#Mi constante no se puede modificar 
print(MI_CONSTANTE)
MI_CONSTANTE=" Nuevo valor"
print(MI_CONSTANTE)
print(Matematicas.PI) #Se llama la constante a traves de la clase

