#Metodo join

'''Se une todos los elmentos'''

tupla=("Hola","Mundo","Universidad","python")
resultado=' '.join(tupla)
print(resultado)

lista=["java", "python","angular","html"]
resultado=','.join(lista)
print(resultado)

cadena="HolaMundo"
mensaje='.'.join(cadena)
print(mensaje)

diccionario={'nombre':'yamith','apellido':'cuervo','edad':'30'}
llaves=' '.join(diccionario.keys())
valores=' '.join(diccionario.values())

print(f"llavers: {llaves}, type: {type(llaves)}")
print(f"valores: {valores}, type: {type(valores)}")