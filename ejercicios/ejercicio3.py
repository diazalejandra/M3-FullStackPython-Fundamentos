#Escriba un programa que calcule el máximo común divisor entre dos números enteros
#¿Qué es el máximo común divisor?
#Se denomina máximo común divisor o MCD al mayor número que divide exactamente a dos o más números a la vez. 

def mcd(x, y):
    if(y==0):
        return x
    else:
        return mcd(y,x%y)

while(True):
    try:
        numero1 = int(input("Ingrese un número entero: "))
        numero2 = int(input("Ingrese un número entero: "))
        print (f"El MCD entre {numero1} y {numero2} es:",end=" ")
        print (mcd(int(numero1),int(numero2)))
        break
    except ValueError:
        print("Ingrese un valor numérico")