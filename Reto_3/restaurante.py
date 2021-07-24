
billete5, billete10, billete20, billete50, billete100, billete200, billete500 = 5, 10, 20, 50, 100, 200, 500

platos = []
precio_cliente = []

menu = {'1' : ['ensalada de tomate y lechuga',2], '2' : ['croquetas de pollo',3], '3' : ['tabla de quesos variados',3], '4' : ['filete de ternera',5], '5' : ['cocido madrileño',4], '6' : ['paella una persona',5], '7' : ['sopa de marisco',3], '8' : ['flan de huevo',2], '9' : ['helado de vainilla',2]}

print(menu)

print(f'''
============================================
            MENÚ DEL DÍA

1 - ensalada de tomate y lechuga:   2 EUROS
2 - croquetas de pollo:             3 EUROS
3 - tabla de quesos variados:       3 EUROS
4 - filete de ternera:              5 EUROS
5 - cocido madrileño:               4 EUROS
6 - paella una persona:             5 EUROS
7 - sopa de marisco:                3 EUROS
8 - flan de huevo:                  2 EUROS
9 - helado de vainilla:             2 EUROS

============================================
''')
while True:
    try:
        seleccion = input('Elija el plato por su número y presione Enter.\nCuando haya acabado de elegir, presione Enter de nuevo: ')
        if not seleccion:
            break
        platos.append(menu[seleccion][0])
        precio_cliente.append(menu[seleccion][1])
    except KeyError:
        print('Esa selección de plato no es correcta. Por favor, introduzca el número de plato correcto.\n')

print(platos)
print(precio_cliente)
print(f'El precio de su menú es: {sum(precio_cliente)}')