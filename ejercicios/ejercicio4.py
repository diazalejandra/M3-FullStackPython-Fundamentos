# Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
# Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio),
# forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.
import math

while (True):
    numero = input(f"Ingrese un mes (1-12): ")
    if numero.isdigit():
        if 1 <= int(numero) <= 12:
            mes = int(numero)
            break
        else:
            print("Ingrese un número entre 1-12")
    else:
        print("Ingrese un número entre 1-12")


print(f"El trimestre correspondiente al mes {mes} es {math.ceil(mes/3)}")
