#Reto 3 terminal de transporte
viaje=str(input(""))

viajes=viaje.split()

viajesListas = "".join(viajes) + "  "

viajes = str(viajes)
# separacion=" ".join(viajesListas)

#Contar las frecuencias de las lista de transporte
caracteres=[]
frecuenciaLista=viajesListas[0] 
x_anterior=" "
frecuencia=0
contador = 0
lista_frecuencias =[]
for x in viajesListas[0:]:   
   if x!=x_anterior:
      x_anterior=x
      caracteres.append(x)

print(" " .join(caracteres))
   
for x in viajesListas: 
   if frecuenciaLista == x:
      contador+=1
   else:     
      print(contador, end=" ")   
      contador=1
   frecuenciaLista=x















   # if x==x_anterior:      
   #    frecuencia=frecuencia+1
   #    frecuenciaLista.append(frecuencia)
# print(caracteres)







 # print(list(zip(frecuencia,viajesListas))) #mapear las frecuencias y cada elemento de la lista     
      
      



      




   # frecuencia.append(viajesListas.count(x))
   # if x == "A":
   #    suma=viajesListas[x]+viajesListas[x]
   # print(str(suma))
   
      

# print(str(viajesListas) + "\n"+ str(frecuencia))


     






# inter=set(viajesListas)

# z=inter.intersection(inter)
# print(z)







# print(viajes)

# conteo = " ".join(viajes)
# print(conteo)