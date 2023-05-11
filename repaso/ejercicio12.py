nombre = input("Indicar su nombre: ")
sexo = input("Ingrese su sexo (f/m): ")

if (sexo.upper() == 'F' and nombre[0].upper() < "M") or (sexo.upper() == 'M' and nombre[0].upper() > "N"):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")