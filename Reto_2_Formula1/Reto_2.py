alejandro=str(input(""))
carolina = str(input(""))
escuderiasGanadoras = str(input(""))

puntajeAlejandro= 0
puntajeCarolina=0
puntaje1=""


for x in escuderiasGanadoras: 
    
    for y in alejandro:      
        
        if y == x:
            puntajeAlejandro = puntajeAlejandro + 1
            # print("alejandro", puntajeAlejandro)
    # print("y",puntajeAlejandro)
    # print("z",puntajeCarolina)
    
    for z in carolina:
        if z == x:
            puntajeCarolina = puntajeCarolina + 1
           
    # print("y",puntajeAlejandro)
    # print("z",puntajeCarolina)
    

# print(puntajeAlejandro)
# print(puntajeCarolina)

    def puntaje():
        if puntajeAlejandro > puntajeCarolina: 
            return str("A")                                   
        if puntajeAlejandro < puntajeCarolina:
            return str("C")
        if puntajeAlejandro == puntajeCarolina:
            return str("E") 
    
    puntaje()   
      

    # print(puntaje(),end="") 
    puntaje1+=puntaje()


print(puntaje1)



 