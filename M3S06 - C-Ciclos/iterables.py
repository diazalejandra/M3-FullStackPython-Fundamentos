#En python son iterables las listas, diccionarios, string.
words = "Esto es una cadena de texto "

for letter in words.split():
    print(letter)

#Forma artesanal
word = ''
for letter in words:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''
print('\n----------------')
for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break
print('\n----------------')
animals_list = ['Gato', 'Perro', 'Pájaro', 'Ardilla']
for animal in animals_list:
    print(animal)

#Función built-in range()
list1 = range(3)
print(type(list1))

for number_in in range(0,10,2): #inicio, término, pasos (si no se pone nada, por defecto es 1)
    print(number_in)

print('\nTablas de multiplicar')
for num_tabla in range(1,11):
    print(f'\nTabla del {num_tabla}')
    for num_mul in range(1,10):
        print(f'{num_tabla} x {num_mul} =', end=' ')
        print(num_tabla * num_mul)

