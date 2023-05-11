# 1. Cree un programa que encuentre el promedio de los tres puntajes dados
#    y devuelva el valor de la letra asociada con esa calificación, de acuerdo con la siguiente tabla:
#    0   - 2    D
#    2.1 - 5    C
#    5.1 - 6    B
#    6.1 - 7    A

i = 0
valores = 3
puntaje = 0

while i < valores:
    try: 
        puntaje += float(input(f"Ingrese el puntaje {i+1}: "))
        i += 1
    except ValueError:
        print("Ingrese un valor numérico")

promedio = puntaje/valores

if 0 <= promedio <= 2:
    clasificacion = 'D'
elif 2 < promedio <= 5:
    clasificacion = 'C'
elif 5 < promedio <= 6:
    clasificacion = 'B'
elif 6 < promedio <= 7:
    clasificacion = 'A'
else:
    clasificacion = '[fuera de rango]'

print(f"\nLa clasificación es {clasificacion}")
