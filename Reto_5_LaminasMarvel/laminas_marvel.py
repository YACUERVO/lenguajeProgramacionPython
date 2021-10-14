
def lista_clases(clases):
    resultado = []
    # Algoritmo
    for item in clases:
        if item not in resultado:
            resultado.append(item)
    return(resultado)


def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
    resultado = []
  # Algoritmo
    for elemento in indices:
        for item in range(len(clases)):
            if item == elemento and clases[item] == clase_a_verificar:
                resultado.append(elemento)
    return(resultado)


def laminas_faltantes(laminas_persona_1, laminas_persona_2):
    resultado = []
  # Algoritmo
    for laminas_2 in laminas_persona_2:
        for laminas_1 in laminas_persona_1:
            if laminas_2 == laminas_1:
                laminas_persona_1.remove(laminas_2)

    resultado=laminas_persona_1

    return(resultado)

def cantidad_laminas_cambiables(laminas_persona_1, laminas_persona_2):
    resultado = 0   
    
  # Algoritmo
    set1 =set(laminas_persona_1)
    set2 =set(laminas_persona_2)
    set3=set1 & set2
    set3=list(set3)
    len(set3)
    len(laminas_persona_1)
    len(laminas_persona_2)
    a=(len(set3)-len(laminas_persona_1))*-1
    b=(len(set3)-len(laminas_persona_2))*-1   

    resultado=min(a,b)

    return resultado   
        
 
