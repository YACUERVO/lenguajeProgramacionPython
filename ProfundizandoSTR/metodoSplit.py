#Metodo split regresa una lista de palabras

cursor="java python javasScript angular spring Excel"
lista=cursor.split()
print(len(lista))
print(lista)

cursosSeparadosComa="java,python,javasScript,angular,sring,excel"
lista=cursosSeparadosComa.split(',')
print(len(lista))
print(lista)

cursosSeparadosComa="java,python,javasScript,angular,sring,excel"
#Para mirar el maximo de separaciones de la lista 
lista=cursosSeparadosComa.split(',',2)
print(len(lista))
print(lista)


