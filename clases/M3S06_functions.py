def saludar(first_name, last_name):
    print (f'Hola {first_name} {last_name}!!!')

def multiplicar_texto(texto, multiplier = 2):
    print(texto * multiplier)

def varieltal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)

def varieltal_dos(param1, **others):
    print(param1)
    print(others)

saludar(last_name='Lujano', first_name='Richar')
multiplicar_texto('V', 5)
multiplicar_texto('X')

varieltal("1A", "2B", 0, "XX", [0, 1])
varieltal_dos("1A", id = 0, name="Carlos")

