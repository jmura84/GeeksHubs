class Animal():
    # Propiedades
    especie = ''
    peso = ''
    altura = ''

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



class Mascota(Animal):
    # Constructor
    def __init__(self, especie, peso, altura):
        super().__init__(especie, peso, altura)

    # Métodos
    def sentarse(self):
        print(f'{self.especie} se sienta')
    def tumbarse(self):
        print(f'{self.especie} se tumba')


leon = Leon('León africano', '250', '1,20')

leon.cazar()
leon.comer()
leon.dormir()
print(leon.especie)
print(leon.peso)

perro = Mascota('Mastín', '50', '1')

perro.sentarse()
perro.tumbarse()
perro.cazar()