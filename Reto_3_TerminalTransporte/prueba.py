#Reto 3 terminal de transporte
viaje=str(input(""))

viajes=viaje.split()

viajesListas = viajes

viajes = str(viajes) + "--"
# separacion=" ".join(viajesListas)

#Contar las frecuencias de las lista de transporte
caracteres=[]
frecuenciaLista=viajesListas[0] 
x_anterior=" "
frecuencia=0
contador = 0
for x in viajesListas[0:]:   
   if x!=x_anterior:
      x_anterior=x
      caracteres.append(x)

print(" " .join(caracteres))
   
for x in viajesListas[0:]: 
   if x == frecuenciaLista:
      contador+=1
   else:
            
      print(contador,end=" ")
      contador=1
   frecuenciaLista=x
