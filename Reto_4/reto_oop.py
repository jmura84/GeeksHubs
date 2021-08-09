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
        self.set_horas_estimadas(horas_estimadas)
        self.set_genero(genero)
        self.set_compañia(compañia)

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


bokunohero = Serie('Boku no Hero Academia', 5, 'Anime shonen', 'Kohei Horikoshi')

print(bokunohero.titulo)
print(bokunohero.genero)
print(bokunohero.temporadas)
print(bokunohero.creador)
print(bokunohero.entregado)