




cantidadAprendices=500

contador = 0

while contador < cantidadAprendices:
    documento=input("Ingrese documento de identidad ")
    nombreApellido=input("Ingrese nombre y apellido ")
    lineaTecnologica=(input("Ingrese si pertenecer a una linea tecnologica SI/NO "))
    estrato = int(input("Ingrese el estrato "))
    raza=input("Ingrese la Raza ")
    edad=int(input("Ingrese la edad "))

    if (estrato < 3) and lineaTecnologica == "si" and raza == "I":
            print("Se otorgara un portatil y una beca para estudiar en una univerdidad. En este caso no podra obtener ningun otro beneficio")
    else: 
        if (estrato == 1):
            bono = 1200000
            print(f"Se le otorgara un bono de {bono} por pertenecer al estrato 1. En este caso no podra obtener ningun otro beneficio" )
        else:        
            if (estrato == 2):
                bono = 400000
                print(f"Se les otorgara un bono de {bono} por pertenecer al estrato 2. Es acumulable")
            elif (estrato == 3):
                bono = 300000
                print(f"Se les otrogara un bono de {bono} por pertenecer al estrato 3. Es acumulable")
            elif (estrato == 4):
                bono = 150000
                print(f"Se les otorgara un bono de {bono}por pertenecer al estrato 4. Es acumulable")
            elif (estrato == 5 and estrato == 6):
                print("No tiene beneficios por ser del estrato 5 y 6")
            if (raza== "I"):
                bono=400000
                print(f"Se les otorgara un bono de {bono} por ser Indigena. Es acumulable")
            elif (raza == "M"):
                bono=250000
                print(f"Se les otorgara un bono de {bono} por ser Mestizo. Es acumulable")
            elif (raza=="N"):
                bono=150000
                print(f"Se les otorgara un bono de {bono} por ser Negro. Es acumulable")
            if (lineaTecnologica == "si"):
                print("Se les otorgara una tablet por pertenecer linea tecnologica. Es acumulable")

   
    if (edad <= 18):
        print("Se les otorgara una orden de almuerzos por ser menores de 18 años")

    contador = contador + 1 



