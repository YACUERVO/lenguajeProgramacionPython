#Dar formtao a str

nombre="Yamith"
edad=30
mensajeFormto="mi nombre es %s y tengo %d"%(nombre,edad)
print(mensajeFormto)


persona=("Karla","Gomez",5000.00)
mensajeFormto="Hola %s %s. Tu sueldo es %.2f"%persona
print(mensajeFormto)

mensajeFormto="Hola %s %s. Tu sueldo es %.2f"
print(mensajeFormto%persona)

nombre="Milena"
edad=28
sueldo=1200000.00
mensaje="F1 Nombre {} edad {} sueldo {:.2f}".format(nombre,edad,sueldo)
print(mensaje)

mensaje="F2 Sueldo {2:.2f} Nombre {0} edad {1} ".format(nombre,edad,sueldo)
print(mensaje)

mensaje='F3 Nombre {n} edad {e} sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
print(mensaje)

diccionario={'nombre':'yamith','edad':35,'sueldo':'5000000'}
mensaje='F4 Nombre {dic[nombre]} edad {dic[edad]}'.format(dic=diccionario)
print(mensaje)

