#Tipo numerico. falso 0, y cualquier otro valor true
valor=0
resultado=bool(valor)
print(f"valor: {valor} resultado: {resultado}")

valor=1
resultado=bool(valor)
print(f"valor: {valor} resultado: {resultado}")

#tipo str. falsp para " ", ture demas valores
valor=""
resultado=bool(valor)
print(f"valor: {valor} resultado: {resultado}")

valor="Hola"
resultado=bool(valor)
print(f"valor: {valor} resultado: {resultado}")

#Tipo coeleccion, false coleccione vacias, true para todas las demas colecciones
valor=[]
resultado=bool(valor)
print(f"valor: {valor} resultado: {resultado}")

valor=[1,2]
resultado=bool(valor)
print(f"valor: {valor} resultado: {resultado}")

if bool(""):
    print("Regreso verdadero")
else:
    print("Regreso falso")