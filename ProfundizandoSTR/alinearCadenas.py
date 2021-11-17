#Alinear cadenas

titulo="Sitio web de Yamith Cuervo"
print(titulo.center(70,'*'))
print(titulo.center(len(titulo)+10,'-'))


#Alinear justifcar a la izquierda
print(titulo.ljust(50,'*'))

#Alinar justifica a la derecha
print(titulo.rjust(50,'-'))

#reemplazar contenido en un str
print(titulo.replace(' ',','))

#elminar caracteres al inicio y final de un str
titulo_1=' ***Milena la vendedora*** '
print(titulo_1.strip())

titulo_1 ="***yamith el desarrollador***".strip('*')
print(titulo_1)

titulo_1="***yamith el ingeniero***".rstrip('*')
print(titulo_1)

titulo_1="***yamith el ingeniero***".lstrip('*')
print(titulo_1)

titulo_1=' *** Milena la vendedora *** '.strip().strip('*').strip()
print(titulo_1)

