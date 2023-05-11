interes = 0.04

monto_inicial = int(input("Ingrese el monto inicial: "))

saldo_ano_1 = (monto_inicial*interes)+monto_inicial
saldo_ano_2 = (saldo_ano_1*interes)+ saldo_ano_1
saldo_ano_3 = (saldo_ano_2*interes)+saldo_ano_2

print(f"Saldo año 1: {round(saldo_ano_1,2)}")
print(f"Saldo año 2: {round(saldo_ano_2,2)}")
print(f"Saldo año 3: {round(saldo_ano_3,2)}")