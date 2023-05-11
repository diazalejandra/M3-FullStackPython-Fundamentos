#Cree una función notaFinal, que calcule la nota final de un estudiante en función de dos parámetros: 
#una nota para el examen y una cantidad de proyectos completados.

#Esta función debe tomar dos argumentos: examen - calificación del examen (de 0 a 100); 
#                                        proyectos - número de proyectos completados (de 0 en adelante);

#Esta función debería devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:
#- 100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
#- 90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
#- 75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.

def notaFinal(nota_examen, cant_proyectos):
    if nota_examen >= 90 or cant_proyectos >= 10:
        return 100
    elif nota_examen >= 75 and cant_proyectos > 5:
        return 90
    elif nota_examen >= 50 and cant_proyectos > 2:
        return 75
    else:
        return 0

while(True): 
    try: 
        nota_examen = float(input("Ingrese la nota del examen: "))
        cant_proyectos = int(input("Ingrese la cantidad de proyectos completados: "))
        print(f"\nLa calificación final es {notaFinal(nota_examen, cant_proyectos)}")
        break
    except ValueError:
        print("Ingrese un valor numérico")