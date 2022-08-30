codigo=input("Ingrese codigo del libro: ")
nombre=input("Ingrese nombre del libro: ")
autor=input("Ingrese el autor del libro: ")
tipoLectura=input("Ingrese tipo de lectura: ")
valor=int(input("Ingrese el valor del libro: "))


total=0
ValorIva=0
contador = 0

while contador <= 100:
        if tipoLectura =="A" and valor > 50000:
                total+= valor - (valor * 0.07)
                ValorIva+=(total * 0.19) + total
                print(f"Valor del libro A {total}")
                print(f"Valor del libro con IVA {ValorIva}")
        elif tipoLectura =="B" and valor > 35000:
                total+= valor - (valor * 0.05)
                ValorIva+=(total * 0.19) + total
                print(f"Valor del libro B {total}")
                print(f"Valor del libro con IVA {ValorIva}")
        elif tipoLectura =="C":
                ValorIva+=(total * 0.19) + total
                print("No se hace descuento")
                
        contador+=1


 


