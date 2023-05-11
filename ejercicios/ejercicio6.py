#Se le ha asignado un tarea para programar un algoritmo para una lavadora, 
#debe investigar cuanta agua se necesita para lavar prendas con las siguientes características: 
#*algodon*, *nilon*, *poliester*. 
#Debe investigar para una lavadora de xx kg cuantas prendas de cada una puede
#lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente
#Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, 
#entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.
#Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
#La función aceptará 2 argumentos: carga lavadora y ropa.

def calcular_agua(carga_lavadora, cantidad_ropa, tipo_tela):
    agua_necesaria = telas[tipo_tela] * 1.1 ** (cantidad_ropa / carga_lavadora)
    return round(agua_necesaria,2)

telas = {"algodon": 5, "nylon": 4, "poliester": 3}

while(True):
    try:
        carga_lavadora = float(input("Ingrese carga de lavadora (kg): "))
        cantidad_ropa = float(input("Ingrese cantidad de ropa: "))
        tipo_tela = input("Ingrese el tipo de tela (algodon, nylon o poliester): ")
        if tipo_tela not in telas:
            print("Tipo de tela no válido")
        else:
            agua = calcular_agua(carga_lavadora, cantidad_ropa, tipo_tela)
            print(f"\nLa cantidad de agua que se necesita para lavar es {agua} lts.")
            break
    except ValueError:
        print("Ingrese un valor numérico")