#Desempaquetado en python
valores=1,2,3
print(valores)
print(type(valores))

valor1,valor2,valor3=1,2,3
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
print(valor3)
print(type(valor3))

#Para no asiganar el valor a la variable
valor1,_,valor3=1,2,3
print(valor1 , valor3)

valor1,valor2,*valor3=1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3)


valor1,valor2,*valor3,valor4,valor5=1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3,valor4,valor5)

valor1,valor2,*valor3,valor4,valor5=[1,2,3,4,5,6,7,8,9]
print(valor1,valor2,valor3,valor4,valor5)

def regresaVariosDatos():
    return 1,2,3

valor1,valor2,valor3=regresaVariosDatos()
print(valor1,valor2,valor3)

#help(str.partition)

hora,separador,minutos='17:20'.partition(':')
print(hora,separador,minutos)
print(hora,_,minutos)
