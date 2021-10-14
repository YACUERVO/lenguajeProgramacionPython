class Aritmetica:
    def __init__(self,numero_1,numero_2):
        self.numero_1=numero_1
        self.numero_2=numero_2

    def sumar(self):
        total=self.numero_1+self.numero_2
        return total
    def restar(self):
        total=self.numero_1-self.numero_2
        return total
    def multiplicar(self):
        total=self.numero_1*self.numero_2
        return total
    def dividir(self):
        total=self.numero_1/self.numero_2
        return total



#crear objeto
aritmetica_1=Aritmetica(5,6)
#objeto y llamar metodo
print(f'''
suma: {aritmetica_1.sumar()}
restar: {aritmetica_1.restar()}
multiplicar: {aritmetica_1.multiplicar()}
dividir: {aritmetica_1.dividir():.2f}
    


''')

#dividir: {aritmetica_1.dividir():.2f formato para imprimir dos dijitos


