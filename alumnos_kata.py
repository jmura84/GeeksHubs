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
    Nombre = []
    Nota = 0

    def __init__(self, *nombre):
        self.Nombre.append(nombre)

    def AñadirNota(self, nota):
        if nota >= 0 and nota <= 10:
            self.Nota = nota
        else:
            self.Nota = 0
            raise ValueError('La nota debe ser 0 o mayor y no puede ser mayor de 10.')





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


#jose.Nombre = 'José'
#jose.Apellidos = 'Pérez Martínez'
#jose.Dni = '94839294M'
#jose.Edad = 20


