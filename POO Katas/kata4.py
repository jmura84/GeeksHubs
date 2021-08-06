class Alumno():
    # Propiedades
    nombre = ''
    apellidos = ''
    __dni = ''
    edad = 0
    nota = 0
    asignaturas = []
    _id = 0

    # Constructor
    def __init__(self, nombre, apellidos, dni, edad, id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__dni = dni
        self.edad = edad
        self._id = id

    # Get / Set
    @property
    def id(self):
        return self._id
    @property
    def dni(self):
        return self.__dni

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
        self.edad += 1

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
        self.nota(nombre, nota)
        self.__id = id

    # Métodos
    @property
    def id(self):
        return self.__id
    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nombre, nota):
        if nota >= 0 and nota <= 10:
            self.__nota = nota
            self.nombre = nombre
            resultado = list((self.nombre, self.__nota))
            print(resultado)
        else:
            self.__nota = 0
            raise ValueError('La nota debe ser 0 o mayor y no puede ser mayor de 10.')



class Clase():
    # Propiedades
    profesor = ''
    alumnos = []
    asignaturas = []

    # Constructor
    def __init__(self, profesor):
        self.profesor = profesor

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



jose = Alumno('José', 'Pérez Martínez', '94839294M', 20, 10)

print(jose.nombre)
print(jose.apellidos)
# print(jose.__dni)
print(jose.edad)

jose.CumplirAños()

print(jose.edad)

jose.Saludar()

jose.nota(9)
print(f'La nota de {jose.nombre} {jose.apellidos} es {jose.nota}.')

jose.AñadirAsignatura('Castellano')
jose.AñadirAsignatura('Mates')
jose.AñadirAsignatura('Historia')
jose.AñadirAsignatura('Geografía')

print(jose.asignaturas)

jose.EliminarAsignatura('Castellano')

castellano = Asignatura('Castellano', 9, 1)

clase_a = Clase('Benito López')

clase_a.AñadirAsignatura('Castellano')
clase_a.AñadirAsignatura('Mates')
clase_a.AñadirAsignatura('Historia')
clase_a.AñadirAsignatura('Geografía')

clase_a.AñadirAlumno('Pepe')
clase_a.AñadirAlumno('Carlos')
clase_a.AñadirAlumno('María')
clase_a.AñadirAlumno('Pedro')
clase_a.AñadirAlumno('Carlos')


clase_a.BorrarAsignatura('Mates')
clase_a.BorrarAlumno('Pepe')


print(clase_a.profesor)
print(clase_a.alumnos, end = ' ')
print(clase_a.asignaturas)

print('El id de José es ' + str(jose.id) + '.')
print(f'El id de la asignatura {castellano.nombre} es {str(castellano.id)}.')
print(f'El DNI de {jose.nombre} es {jose.dni}.')

#jose.nombre = 'José'
#jose.apellidos = 'Pérez Martínez'
#jose.dni = '94839294M'
#jose.edad = 20


