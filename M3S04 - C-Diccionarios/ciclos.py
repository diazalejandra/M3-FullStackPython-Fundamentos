print("======== Trabajando con dicccionarios =======")

empty_dict = {}

fullfiled_ditc = {
    "id": 1,
    "name": "Valeria"
}

print(empty_dict)
print(fullfiled_ditc)

lista_1 = ['a1', 'b2']
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ('a1', 'b2')
print(tupla_1, dict(tupla_1))

list_dimesional = [['a', 1], ['b', 3]]
print(list_dimesional, dict(list_dimesional))

empty_dict_2 = dict()
print(empty_dict_2)

full_dict = dict(
    genero="M",
    nacionalidad="E"
)
print(full_dict)


empleado = {
    "name": "valeria",
    "apellido": "roso",
    "edad": 18,
    "rut": "11.111.111-1"
}

print(empleado)
for variablex in empleado.values():
    print(variablex)

print(empleado)
for clave, valor in empleado.items():
    print(clave, valor)


print("======== Trabajando con consicionales =======")

edad = 60
if edad > 50:
    print("Hola Don")
    print("Hola desde adentro de if")


print("aca continua el codigo")

# Esto es un comentario

temperatura = 38
if temperatura >= 37:
    print("Alerta de temperatura alta")
else:
    print("La temperatura aun es normal")

temperatura = 5
pais = 'Chile'

if temperatura < 10:
    if pais == 'chile':
        print('cccc')
    else:
        print('zzzz')
else:
    if pais == 'chile':
        print('111')
    else:
        print('222')

if temperatura < 10:
    print("Es altamente probable que nieve")
elif temperatura >= 10 and temperatura <= 20:
    print("Es medianamente probable que nieva")
else:
    print("No hay posibilidad de nieve")

print('--- WHILE ---')

want_exit = 'n'
while want_exit == 'n':
    print("Hola, cómo estás?")
    want_exit = input("¿Quieres salir S/N?")
print("Fuera del while")

print('--- WHILE 2 ---')
want_exit = 'n'
num_questions = 0

while want_exit == 'n':
    print("Hola, cómo estás?")
    want_exit = input("¿Quieres salir S/N?")
    num_questions += 1
    if num_questions == 3:
        print("Alcanzaste el máximo permitido")
        break
print("Se acabó el while")