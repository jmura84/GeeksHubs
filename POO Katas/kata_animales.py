class Animal():
    # Propiedades
    especie = ''
    peso = 0
    altura = 0

    # Constructor
    def __init__(self, especie, peso, altura):
        self.especie = especie
        self.peso = peso
        self.altura = altura

    # Métodos
    def comer(self):
        print(f'{self.especie} se dispone a comer')
    def cazar(self):
        print(f'{self.especie} se dispone a cazar')
    def dormir(self):
        print(f'{self.especie} se dispone a dormir')



class Leon(Animal):
    #Constructor
    def __init__(self, especie, altura, peso):
        super().__init__(especie, altura, peso)



class Mascota():
    # Propiedades
    nombre = ''
    amo = ''
    numero_chip = ''

    # Métodos
    def sentarse(self):
        print(f'{self.especie} se sienta')

    def tumbarse(self):
        print(f'{self.especie} se tumba')



class Perro(Animal, Mascota):
    # Constructor
    def __init__(self, especie, peso, altura, nombre, amo, numero_chip):
        Animal.__init__(especie, peso, altura)
        Mascota.__init__(nombre, amo, numero_chip)




leon = Leon('León africano', '250', '1,20')

leon.cazar()
leon.comer()
leon.dormir()
print(leon.especie)
print(leon.peso)

perro = Perro('Mastín', 50, 40, 'Tobi', 'Tomás', '242342342')

perro.sentarse()
perro.tumbarse()
perro.cazar()
print(perro.nombre)