renta_anual = int(input("Indique su renta anual: "))

if renta_anual < 10000:
    print(f"Tienes que pagar el 5% de interés: {round(renta_anual*0.05,2)}")
elif renta_anual >= 10000 and renta_anual < 20000:
    print(f"Tienes que pagar el 15% de interés: {round(renta_anual*0.15,2)}")
elif renta_anual >= 20000 and renta_anual < 35000:
    print(f"Tienes que pagar el 20% de interés: {round(renta_anual*0.2,2)}")
elif renta_anual >= 35000 and renta_anual < 60000:
    print(f"Tienes que pagar el 30% de interés: {round(renta_anual*0.3,2)}")
elif renta_anual >=  60000:
    print(f"Tienes que pagar el 45% de interés: {round(renta_anual*0.45,2)}")