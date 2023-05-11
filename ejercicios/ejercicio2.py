#Utilizando dos while anidados, construya la tablas de mutiplicacion

def tablas_de_multiplicar(start, end):
    i = start
    while i <= end:
        j = start
        print(f"\nTabla del {i}: ")
        while j <= end:
            print(f"{i} x {j} = {i*j}")
            j += 1
        i += 1

tablas_de_multiplicar(1,10)