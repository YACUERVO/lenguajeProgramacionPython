class Productos:
    contador_productos=0
    def __init__(self, productos, codigos, clase,competencia):
        Productos.contador_productos+= 1
        self._IDProductos=Productos.contador_productos
        self._productos=list(productos)
        self._codigos=codigos
        self._clase=clase
        self._competencia=list(competencia)

    def tipos_productos(self):
        lista_productos =[]
        for producto in self._productos:            
                if producto not in lista_productos:
                    lista_productos.append(producto)
        print(lista_productos)
        
    def productosFaltantes(self):
        lista_prodcutos=[]
        for codigo in self._codigos:
            for producto in range(len(self._productos)):       
                if producto == codigo and self._productos[producto] == self._clase:
                    lista_prodcutos.append(producto)
        print(lista_prodcutos)

    def novendo(self):
        lista_productos=[]
        for producto_competencia in self._competencia:
            for producto_restaurante in self._productos:
                if producto_competencia != producto_restaurante:
                    if producto_competencia not in lista_productos:
                        lista_productos.append(producto_competencia)
        print(lista_productos)
        
    def intercambio(self):
        resultado= 0
        set1=set(self._productos)
        set2=set(self._competencia)        
        set3=set1 & set2
        set3=list(set3)
        len(set3)
        len(self._productos)
        len(self._competencia)
        a=(len(set3)-len(self._productos))*-1
        b=(len(set3)-len(self._competencia))*-1   
        resultado=min(a,b)
        print(resultado)   

 
#Obejto de lista de productos
producto_1=Productos(["carnes", "carnes", "lacteos", "verduras", "frutas", "lacteos", "carnes", "verduras", "verduras", "carnes"],[1,2,6,8],"carnes",["pasas","papas","queso","galletas"])

producto_2=Productos(["pasas","leche","papas","carne","queso","galletas"],[1,2,5],"queso", ["frutas","carne","leche","huevos"])


#Metodo para agregar elementos que no estan en la lista
producto_1.tipos_productos()

#Metodo productos faltante
producto_1.productosFaltantes()

#Metodo competencia
producto_1.novendo()

#Metodo intercambio
producto_2.intercambio()