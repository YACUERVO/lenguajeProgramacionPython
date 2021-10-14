#Ejercicio Policita de transito

tieneLicencia=int(input("Tiene licencia de conducir (Si = 1) o (No = 0)  "));
cantidadMultas = int(input("Ingrese la cantidad de multas:  "));
gradosAlcohol = float(input("cantidad de grados de alcohol:  "));
velocidadVehiculo = int(input("Velosidad del carro:  "));
papelesRegla = int(input("tiene papeles en regla (Si = 1) o (No = 0)  "));
vidriosPolarizados = int(input("tiene los vidrios polarizados (Si = 1) o (No = 0) "))
edad = int(input("introduzca tu edad  "))



# def tiene_licencia():   
#     if  tieneLicencia ==1:         
#         return ("Tiene licencia de conducir")
#     elif tieneLicencia == 0:
#         return ("no tiene licencia de conducir")       
#     else:
#          tieneLicencia >= 2        
#          return ("introduciste un numero incorrecto para la licencia")
        
      

# def papeles_regla(x):
#     if x == 1:
#         return("Si tiene los papeles en regla")
#     elif x==0:
#         return("no tiene los papeles en regla")
#     else:
#         x>=2
#         return ("introduciste un numero incorrecto para los papeles")
    

# def vidrios_polarizados(x):
#     if x==1:
#         return("Si tiene vidrios polarizados")
#     elif x==0:
#         return("No tiene vidrios polarizados")
#     else:
#         x>=2
#         return("introduciste un numero incorrecto para vidrio polarizados")
   

def puede_conducir():    
    if tieneLicencia == 1 and cantidadMultas == 0 and gradosAlcohol ==0 and velocidadVehiculo <= 80 and papelesRegla == 1 and vidriosPolarizados ==0 and edad > 18:
        return("puedes continuar con tu camino")
    else:
        return("no puedes conducir, sacar multa")
    
    
# print(tiene_licencia());
# print(papeles_regla(papelesRegla));
# print(vidrios_polarizados(vidriosPolarizados));
print(puede_conducir())
