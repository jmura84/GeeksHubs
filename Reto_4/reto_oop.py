class Serie():
    # Propiedades
    __titulo = ''
    __temporadas = 3
    entregado = False
    __genero = ''
    __creador = ''

    # Constructor
    def __init__(self, titulo, temporadas, genero, creador):
        self.__titulo = titulo
        self.__temporadas = temporadas
        self.__genero = genero
        self.__creador = creador
    # Get / Set
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def set_titulo(self, titulo):
        self.__titulo = titulo
    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def set_temporadas(self, temporadas):
        self.__temporadas = temporadas
    @property
    def genero(self):
        return self.__genero
    @temporadas.setter
    def set_genero(self, genero):
        self.__genero = genero
    @property
    def creador(self):
        return self.__creador
    @creador.setter
    def set_creador(self, creador):
        self.__creador = creador

    # Métodos



class Videojuego():
    # Propiedades
    __titulo = ''
    __horas_estimadas = 10
    entregado = False
    __genero = ''
    __compañia = ''

    def __init__(self, titulo, horas_estimadas, genero, compañia):
        self.set_titulo(titulo)
        self.__horas_estimadas = horas_estimadas
        self.__genero = genero
        self.__compañia = compañia

    # Get / Set
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def set_titulo(self, titulo):
        self.__titulo = titulo
    @property
    def horas_estimadas(self):
        return self.__horas_estimadas
    @horas_estimadas.setter
    def set_horas_estimadas(self, horas_estimadas):
        self.__horas_estimadas = horas_estimadas
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def set_genero(self, genero):
        self.__genero = genero
    @property
    def compañia(self):
        return self.__compañia
    @compañia.setter
    def set_compañia(self, compañia):
        self.__compañia = compañia

    # Métodos



class Entregable():
    # Métodos
    def entregar(self, obj1):
        if obj1.entregado == True:
            print(f'Todavía no se ha devuelto el artículo {obj1.titulo}')
        else:
            obj1.entregado = True
            print(f'¡Artículo {obj1.titulo} entregado!')
    def devolver(self, obj1):
        if obj1.entregado == False:
            print(f'Ya se había devuelto el artículo {obj1.titulo}')
        else:
            obj1.entregado = True
            print(f'¡Artículo {obj1.titulo} devuelto!')
    def is_entregado(self, obj1):
        if obj1.entregado == True:
            print(f'El artículo {obj1.titulo} está en estado entregado')
        else:
            print(f'El artículo {obj1.titulo} está en estado devuelto')
    def compareTo(self, obj1, obj2):
        pass




bokunohero = Serie('Boku no Hero Academia', 5, 'Anime shonen', 'Kohei Horikoshi')

print(bokunohero.titulo)
print(bokunohero.genero)
print(bokunohero.temporadas)
print(bokunohero.creador)
print(bokunohero.entregado)

interfaz = Entregable()

interfaz.entregar(bokunohero)
interfaz.entregar(bokunohero)
interfaz.is_entregado(bokunohero)
print(bokunohero.entregado)

# guiltygear = Videojuego('Guilty Gear Strive', 150, 'Lucha', 'Arc System Works')
#
# print(guiltygear.titulo)
# print(guiltygear.horas_estimadas)
# print(guiltygear.genero)
# print(guiltygear.compañia)
# print(guiltygear.entregado)
#
# guiltygear.set_titulo('Dragon Ball FighterZ')
# print(guiltygear.titulo)