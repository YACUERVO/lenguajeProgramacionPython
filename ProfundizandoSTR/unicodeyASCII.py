# #Caracter UNICODE
# print("Hola\u0020Mundo")
# print('notacion simple:','\u0041')
# print('notacion extendida:', '\U00000041')
# print("notacion hexadecimal", '\x41')
# print("Corazon",'\u2665')
# print("cara sonriendo",'\U0001f600')
# print("Serpiente",'\U0001F40D')

# #caracteres ASCII
# caracter=chr(65)
# print(f'caracter {caracter}')

# caracter=chr(64)
# print(f'caracter {caracter}')

# caracter=chr(97)
# print(f'caracter {caracter}')

#Caracters bytes
caracterresBytes= b'hola mundo'
print(caracterresBytes)

mensaje =b'Universidad'
print(mensaje[0])
print(chr(mensaje[0]))

string="programación con pyhon"
print("string original", string)
bytes=string.encode("UTF-8")
print("bytes codificado",bytes)

#convertir bytes a str
string2=bytes.decode("UTF-8")
print('string decodificado', string2)
print(string==string2)