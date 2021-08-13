'''
Este módulo es una práctica de programación orientada a objetos que incluye las clases Serie, Videojuego y Entregable.
La clase entregable contiene también el método compareTo que sirve para comparar el número de horas estimadas y
el número de temporadas según el tipo de objeto.
'''

__author__ = 'Javier Muñoz Ramón'
__copyright__ = 'Copyright (c) 2021. All rights are reserved.'
__license__ = 'GPL 3'

class Serie():
    '''
    Clase que define los objetos de tipo serie, sus características y su estado de entrega.
    '''
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

    def __str__(self):
        return f'Esta serie llamada {self.titulo} tiene {str(self.temporadas)} temporadas, es del género {self.genero} y su creador es {self.creador}'

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
    '''
    Clase que define los objetos de tipo videojuego, sus características y su estado de entrega.
    '''
    # Propiedades
    __titulo = ''
    __horas_estimadas = 10
    entregado = False
    __genero = ''
    __compañia = ''

    # Constructor
    def __init__(self, titulo, horas_estimadas, genero, compañia):
        self.__titulo = titulo
        self.__horas_estimadas = horas_estimadas
        self.__genero = genero
        self.__compañia = compañia

    def __str__(self):
        return f'Este videojuego llamado {self.titulo} dura aproximadamente {str(self.horas_estimadas)} horas, es del género {self.genero} y pertenece a la compañía {self.compañia}'

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
    '''
    Clase que define el estado de entrega de los objetos serie o videojuego. Además tiene el método para ver el estado actual.
    También incluye el método compareTo para comparar la las horas estimadas de dos videojuegos o las temporadas de dos series.
    '''
    # Métodos
    def entregar(self, obj1):
        '''
        Cambia el estado del artículo a entregado si este ha sido devuelto.
        Input: objeto
        Output: None
        '''
        if obj1.entregado == True:
            print(f'Todavía no se ha devuelto el artículo {obj1.titulo}')
        else:
            obj1.entregado = True
            print(f'¡Artículo {obj1.titulo} entregado!')
    def devolver(self, obj1):
        '''
        Cambia el estado del artículo a devuelto si este ha sido entregado.
        Input: objeto
        Output: None
        '''
        if obj1.entregado == False:
            print(f'Ya se había devuelto el artículo {obj1.titulo}')
        else:
            obj1.entregado = False
            print(f'¡Artículo {obj1.titulo} devuelto!')
    def is_entregado(self, obj1):
        '''
        Verifica si el estado del artículo es entregado o devuelto.
        Input: objeto
        Output: None
        '''
        if obj1.entregado == True:
            print(f'El artículo {obj1.titulo} está en estado entregado')
        else:
            print(f'El artículo {obj1.titulo} está en estado devuelto')
    def compareTo(self, obj1, obj2):
        '''
        Compara el número de horas estimadas o el número de temporadas según el tipo de objeto que se compare.
        Input: dos objetos
        Output: None
        '''
        try:
            if type(obj1) and type(obj2) == Serie:
                if obj1.temporadas > obj2.temporadas:
                    print(f'{obj1.titulo} tiene {obj1.temporadas - obj2.temporadas} temporadas más que {obj2.titulo}')
                elif obj1.temporadas < obj2.temporadas:
                    print(f'{obj2.titulo} tiene {obj2.temporadas - obj2.temporadas} temporadas más que {obj1.titulo}')
                else:
                    print(f'{obj1.titulo} y {obj2.titulo} tienen {obj1.temporadas} temporadas')
            elif type(obj1) and type(obj2) == Videojuego:
                if obj1.horas_estimadas > obj2.horas_estimadas:
                    print(f'{obj1.titulo} tiene {obj1.horas_estimadas - obj2.horas_estimadas} horas más de duración que {obj2.titulo}')
                elif obj1.horas_estimadas < obj2.horas_estimadas:
                    print(f'{obj2.titulo} tiene {obj2.temporadas - obj2.temporadas} horas más de duración que {obj1.titulo}')
                else:
                    print(f'{obj1.titulo} y {obj2.titulo} tienen {obj1.horas_estimadas} horas de duración')
        except AttributeError:
            print('Solo se pueden comparar si son de la misma categoría: series o videojuegos')

if __name__ == '__main__':
    bokunohero = Serie('Boku no Hero Academia', 5, 'Anime shonen', 'Kohei Horikoshi')

    print(bokunohero.titulo)
    print(bokunohero.genero)
    print(bokunohero.temporadas)
    print(bokunohero.creador)
    print(bokunohero.entregado)

    # bokunohero.set_titulo('Bleach')
    # bokunohero.titulo = 'Bleach'
    # bokunohero.titulo

    naruto = Serie('Naruto', 3, 'Anime shonen', 'Masashi Kishimoto')
    dragonball = Serie('Dragon Ball', 20, 'Anime shonen', 'Akira Toriyama')
    southpark = Serie('South Park', 26, 'Humor', 'Matt Stone / Trey Parker')
    mandalorian = Serie('Mandalorian', 1, 'Acción', 'Jon Favreau')

    interfaz = Entregable()

    interfaz.entregar(bokunohero)
    interfaz.entregar(bokunohero)
    interfaz.is_entregado(bokunohero)
    print(bokunohero.entregado)

    guiltygear = Videojuego('Guilty Gear Strive', 150, 'Lucha', 'Arc System Works')

    print(guiltygear.titulo)
    print(guiltygear.horas_estimadas)
    print(guiltygear.genero)
    print(guiltygear.compañia)
    print(guiltygear.entregado)

    fighterz = Videojuego('Dragon Ball FighterZ', 150, 'Lucha', 'Arc System Works')
    f12021 = Videojuego('F1 2021', 400, 'Carreras', 'Codemasters / EA')
    overwatch = Videojuego('Overwatch', 1000, 'Shoot-em-up', 'Blizzard / Activision')
    codwarzone = Videojuego('Call of Duty: Warzone', 500, 'Shoot-em-up', 'Blizzard / Activision')

    series = [bokunohero, naruto, dragonball, southpark, mandalorian]

    videojuegos = [guiltygear, fighterz, f12021, overwatch, codwarzone]

    # guiltygear.set_titulo('Dragon Ball FighterZ')
    # print(guiltygear.titulo)

    interfaz.compareTo(series[0], series[1])
    interfaz.compareTo(videojuegos[0], videojuegos[1])
    interfaz.compareTo(series[2], videojuegos[2])

    interfaz.devolver(bokunohero)
    print(bokunohero.entregado)
    interfaz.is_entregado(bokunohero)

    print(bokunohero)
    print(naruto)
    print(guiltygear)
    print(fighterz)