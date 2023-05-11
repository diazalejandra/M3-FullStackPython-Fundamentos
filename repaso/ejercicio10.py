numerador = float(input("Ingrese el numerador: "))
denominador = float(input("Ingrese el denominador: "))

if denominador == 0:
    print("No se puede dividir por 0")
else:
    resultado = numerador/denominador
    print(f"El resultado es {resultado}")