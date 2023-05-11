edad_minima = 16
ingresos_tope = 1000

anos = int(input("Ingrese su edad: "))
ingreso = int(input("Indique su ingreso mensual: "))

if (anos > edad_minima and ingreso >= ingresos_tope):
    print("Paga impuestos")
else:
    print("No paga impuestos")