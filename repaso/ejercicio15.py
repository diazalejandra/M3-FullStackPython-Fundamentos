dinero = 2400
puntuacion = float(input("Indique su puntuación: "))

if puntuacion == 0.0:
    print("Nivel de Rendimiento: Inaceptable")
    print(f"Bono Obtenido: {round(puntuacion*dinero,0)}")
elif puntuacion == 0.4:
    print("Nivel de Rendimiento: Aceptable")
    print(f"Bono Obtenido: {round(puntuacion*dinero,0)}")
elif puntuacion >= 0.6:
    print("Nivel de Rendimiento: Meritorio")
    print(f"Bono Obtenido: {round(puntuacion*dinero,0)}")
else:
    print("Puntuación no valida")