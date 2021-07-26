class Alumno():
    Nombre = ''
    Apellidos = ''
    Dni = ''
    Edad = 0
    Nota = 0

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
            print('La nota debe ser 0 o mayor y no puede ser mayor de 10.')
            self.Nota = 0

    def CumplirAños(self):
        self.Edad += 1

jose = Alumno('José', 'Pérez Martínez', '94839294M', 20)

#jose.Nombre = 'José'
#jose.Apellidos = 'Pérez Martínez'
#jose.Dni = '94839294M'
#jose.Edad = 20

jose.AñadirNota(848)

print(jose.Nombre)
print(jose.Apellidos)
print(jose.Dni)
print(jose.Edad)
print(jose.Nota)

jose.CumplirAños()

print(jose.Edad)
jose.Saludar()
