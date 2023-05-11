mensaje = "Hola Mundo"

print(mensaje.lower())

print(mensaje.replace('Mundo', 'Richar'))

print('---- listas ----')
# Las listas son mutables
# Las listas se crean con {}
empty_list = []
print(empty_list)

fullfiled_list = [1,2,500,1.4,[2,'a'], {'name': 'Richar'}, {1,3,5}]
print(fullfiled_list)

second_list = list()
print(second_list)

print(list('Concurso'))

range_one = range(50)
print(list(range_one))

print('---- agregar ----')
numeros = [1,2,3]
numeros.append(4) #agrega un elemento al final
numeros.insert(2,10) #agrega un elemento en la posicion 2
numeros.extend([4,5,6])

#print(numeros)

print('---- eliminar ----')
#numeros.pop() #elimina el ultimo elemento
#numeros.pop(1) #elimina el elemento en la posicion 1
#numeros.remove(10) #elimina el elemento por su valor
del(numeros[0])
#print(numeros)

print('---- ordernar ----')
numeros.reverse() #ordena la lista de forma inversa
#print(numeros) 
numeros.sort() #ordena la lista de forma ascendente
#print(numeros) 
numeros.sort(reverse=True) #ordena la lista de forma descendente
#print(numeros) 

print('---- recorrer listas ----')
for e in numeros:
    print(e)

#print('---- modificar listas ----')
numeros[0] = 1
for e in range(len(numeros)):
    if numeros[e] == 4:
        numeros[e] = 20
#print(numeros)

print('---- tuplas ----')
# Las tuplas son inmutables
# Las tuplas se crean con ()
# Guardan menos espacio en memoria

empty_tuple = ()
fullfiled_tuple = (1, 'Ale', 90)

print(fullfiled_tuple)

print(type(fullfiled_tuple))
one_tuple = ('juan',)
print(type(one_tuple))

hojas = 'carta', 'oficio' #es una tupla declarada sin parentesis, se puede, pero no se debe
print(type(hojas))

#las tuplas no soportan asignación --> hojas[0] = 'letter'

list_to_convert = [2,6,8,9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)

print('---- reverse ----')
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

Reverse(tuple_converted)
     
print(Reverse(tuple_converted))

#otra opcion
tuple_converted = tuple(reversed(tuple_converted))
print(tuple_converted)

print('---- append ----')
tuple_converted = tuple_converted+(5,)
print(tuple_converted)

print('---- extend ----')
tuple_converted = tuple_converted+(6,7,8)
print(tuple_converted)

print('---- remove ----')
tuple_converted = tuple_converted[1:]
print(tuple_converted)

print('---- sort ----')
tuple_converted = tuple(sorted(tuple_converted, reverse=True))  
print(tuple_converted)

print('---- clear ----')
tuple_converted = tuple()
print(tuple_converted)

