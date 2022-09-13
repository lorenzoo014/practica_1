class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

#----------Herencia de los vehículos de 4 ruedas-------#
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}".format(self.velocidad, self.cilindrada)
c = Coche("azul", 4, 150, 1200)

class Camioneta(Coche):
    def __init__(self,color, ruedas, velocidad, cilindrada,carga):
        Coche.__init__(self, color, ruedas,velocidad,cilindrada)
        self.carga=carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kilos".format(self.carga)

camioneta1 = Camioneta("rojo",4,130,1100,500)

#----------HERENCIA MÚLTIPLE----------#
#----------herencia de los vehiculos de 2 ruedas----------#
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} ".format(self.tipo)

bicicleta1 = Bicicleta("verde",2,"urbana")

class Motocicleta(Bicicleta):
    def __init__(self,color, ruedas, tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}".format(self.velocidad, self.cilindrada)

Motocicleta1 = Motocicleta("naranja",2,"deportiva",120,1000)

lista_vehiculos =[]
lista_vehiculos.append(c)
lista_vehiculos.append(camioneta1)
lista_vehiculos.append(bicicleta1)
lista_vehiculos.append(Motocicleta1)
for vehiculo in lista_vehiculos:
    print(str(vehiculo))


#----------funcion_catalogar----------#
def catalogar(lista):
    for vehiculo in lista:
        informacion = "El vehiculo es un "+ type(vehiculo).__name__+" y sus atributos son: "+ str(vehiculo)
        print(informacion)
print("\nComprobamos la funcion catalogar: ")
catalogar(lista_vehiculos)
print("\n Comprobamos la funcion catalogar con el polimorfismo de sobreecarga correspondiente : ")
#----------funcion_catalogar_polimorfismo_de_sobrecarga----------#
def catalogar(lista, ruedas):
    contador =0
    print("\n")
    for vehiculo in lista:
        informacion = "El vehiculo es un/a "+ type(vehiculo).__name__+" y sus atributos son: "+ str(vehiculo)
        if (vehiculo.ruedas == ruedas):
            contador +=1
            print(informacion)
    # print(contador)
    if(contador ==0):
        print("No hay ningun vehiculo con {} ruedas".format(str(ruedas)))
    print("Por lo tanto, se han encontrado {} vehiculos con {} ruedas".format(str(contador),str(ruedas)))

catalogar(lista_vehiculos, 2)
catalogar(lista_vehiculos, 4)
catalogar(lista_vehiculos, 0)