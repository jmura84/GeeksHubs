class Alumno():
    # Propiedades
    nombre = ''
    apellidos = ''
    __dni = ''
    __edad = 0
    __id = 0
    nota = 0
    asignaturas = []
    _id = 0

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad, id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__dni = dni
        self.__edad = edad
        self.__id = id

    # Get / Set
    @property
    def id(self):
        return self.__id
    @property
    def dni(self):
        return self.__dni
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad <= 100:
            self.__edad = edad
        else:
            raise ValueError('Edad fuera del rango')

    # Métodos
    def Saludar(self):
        print(f'Hola, me llamo {self.nombre} {self.apellidos} y tengo {self.edad} años.')

    def nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.nota = nota
        else:
            self.nota = 0
            raise ValueError('La nota debe ser 0 o mayor y no puede ser mayor de 10.')

    def CumplirAños(self):
        self.__edad += 1

    def AñadirAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def EliminarAsignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            print(self.asignaturas)
        else:
            raise ValueError('La asignatura no estaba en la lista.')



class Asignatura():
    # Propiedades
    nombre = ''
    __nota = 0
    __id = 0

    # Constructor
    def __init__(self, nombre, nota, id):
        self.nombre = nombre
        self.__nota = nota
        self.__id = id

    # Get / Set
    @property
    def id(self):
        return self.__id
    @property
    def nota(self):
        return self.__nota
    @id.setter
    def id(self, id):
        self.id = id
    @nota.setter
    def nota(self, nombre, nota):
        if nota >= 0 and nota <= 10:
            self.__nota = nota
        else:
            self.__nota = 0
            raise ValueError('La nota debe ser 0 o mayor y no puede ser mayor de 10.')



class Aula():
    # Propiedades
    profesor = ''
    alumnos = []
    asignaturas = []
    __id = 0

    # Constructor
    def __init__(self, profesor, alumno, id):
        self.profesor = profesor
        self.alumnos = alumno
        self.__id = id

    # Get / Set
    @property
    def id(self):
        return self.__id

    # Métodos
    def AñadirAlumno(self, alumno):
        self.alumnos.append(alumno)
        print(self.alumnos)

    def BorrarAlumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(self.alumnos)
        else:
            raise ValueError('Este alumno no está en esta clase.')

    def AñadirAsignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        print(self.asignaturas)

    def BorrarAsignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            print(self.asignaturas)
        else:
            raise ValueError('Esta asignatura no está en la lista.')



class Usuario(Aula):
    # Propiedades
    trimestre = 0
    # Constructor
    def __init__(self, profesor, alumno, id, trimestre):
        super().__init__(profesor, alumno, id)
        self.trimestre = trimestre




manu = Alumno('Manu', 'Pérez', '1231411M', 12, 1)

print(manu.edad)
print(manu.id)
print(manu.dni)

manu.edad = 15

print(manu.edad)

castellano = Asignatura('Castellano', 9, 1)

print(castellano.nota)
print(castellano.id)

pepe = Usuario('José', 'Pedro', 2, 3)
print(pepe.profesor)
print(pepe.alumnos)
print(pepe.trimestre)