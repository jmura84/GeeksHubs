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



class Mascota(Animal):
    # Constructor
    def __init__(self, especie, peso, altura):
        super().__init__(especie, peso, altura)

    # Métodos
    def sentarse(self):
        print(f'{self.especie} se sienta')
    def tumbarse(self):
        print(f'{self.especie} se tumba')


perro = Mascota('Mastín', 50, 1)

perro.sentarse()
perro.tumbarse()
perro.cazar()