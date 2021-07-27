class Alumno():
    Nombre = ''
    Apellidos = ''
    Dni = ''
    Edad = 0
    Nota = 0
    Asignaturas = []

    def __init__(self, nombre, apellidos, dni, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Dni = dni
        self.Edad = edad

    def Saludar(self):
        print(f'Hola, me llamo {self.Nombre} {self.Apellidos} y tengo {self.Edad} años.')

    def AñadirNota(self, nota):
        if nota >= 0 and nota <= 10:
            self.Nota = nota
        else:
            self.Nota = 0
            raise ValueError('La nota debe ser 0 o mayor y no puede ser mayor de 10.')

    def CumplirAños(self):
        self.Edad += 1

    def AñadirAsignatura(self, asignatura):
        self.Asignaturas.append(asignatura)

    def EliminarAsignatura(self, asignatura):
        if asignatura in self.Asignaturas:
            self.Asignaturas.remove(asignatura)
            print(self.Asignaturas)
        else:
            raise ValueError('La asignatura no estaba en la lista.')



class Asignatura():
    Nombre = ''
    Nota = 0

    def __init__(self, nombre, nota):
        self.AñadirNota(nombre, nota)

    def AñadirNota(self, nombre, nota):
        if nota >= 0 and nota <= 10:
            self.Nota = nota
            self.Nombre = nombre
            resultado = list((self.Nombre, self.Nota))
            print(resultado)
        else:
            self.Nota = 0
            raise ValueError('La nota debe ser 0 o mayor y no puede ser mayor de 10.')



class Clase():
    Profesor = ''
    Alumnos = []
    Asignaturas = []

    def AñadirAlumno(self, alumno):
        self.Alumnos.append(alumno)
        print(self.Alumnos)

    def BorrarAlumno(self, alumno):
        if alumno in self.Alumnos:
            self.Alumnos.remove(alumno)
            print(self.Alumnos)
        else:
            raise ValueError('Este alumno no está en esta clase.')

    def AñadirAsignatura(self, asignatura):
        self.Asignaturas.append(asignatura)
        print(self.Asignaturas)

    def BorrarAsignatura(self, asignatura):
        if asignatura in self.Asignaturas:
            self.Asignaturas.remove(asignatura)
            print(self.Asignaturas)
        else:
            raise ValueError('Esta asignatura no está en la lista.')



jose = Alumno('José', 'Pérez Martínez', '94839294M', 20)

print(jose.Nombre)
print(jose.Apellidos)
print(jose.Dni)
print(jose.Edad)

jose.CumplirAños()

print(jose.Edad)

jose.Saludar()

jose.AñadirNota(9)
print(f'La nota de {jose.Nombre} {jose.Apellidos} es {jose.Nota}.')

jose.AñadirAsignatura('Castellano')
jose.AñadirAsignatura('Mates')
jose.AñadirAsignatura('Historia')
jose.AñadirAsignatura('Geografía')

print(jose.Asignaturas)

jose.EliminarAsignatura('Castellano')

asignatura = Asignatura('Castellano', 9)

clase_a = Clase()

clase_a.AñadirAsignatura('Castellano')
clase_a.AñadirAsignatura('Mates')
clase_a.AñadirAsignatura('Historia')
clase_a.AñadirAsignatura('Geografía')

clase_a.AñadirAlumno('Pepe')
clase_a.AñadirAlumno('María')
clase_a.AñadirAlumno('Pedro')
clase_a.AñadirAlumno('Carlos')


clase_a.BorrarAsignatura('Mates')
clase_a.BorrarAlumno('Pepe')


#jose.Nombre = 'José'
#jose.Apellidos = 'Pérez Martínez'
#jose.Dni = '94839294M'
#jose.Edad = 20


