#Escribir un programa en el que se pregunte al usuario por una 
#frase y una letra, y muestre por pantalla el numero de veces
#que aparece la letra en la frase

#frase = input("Ingrese una frase o palabra: ")
#letra = input("Ingrese letra a buscar: ")

#print(f"La cantidad de '{letra}' es: {frase.count(letra)}")

#Dato un capital K, a un interes Y (que oscila entre 0 y 100)
#durante Z años y se desea saber en cuanto se habrá convertido
#ese capital en Z años, sabiendo que es acumulativo

# capital = int(input("Ingrese un capital: "))
# interes = int(input("Ingrese el interés (0-100): "))
# anios = int(input("Ingrese cantidad de años: "))

# for a in range(anios):
#     capital += (capital * (interes/100))

# print(f"El capital despues de {anios} años es de {capital}")

#Haz un motor de videojuegos para dos personajes A y B:
#- Empieza el combate y se decide aleatoriamente quien empieza
#- Si ataca A restara su ataqueA y defensaB
#- Cambio de turno. Le toca a B. Realiza el ataque.
#- Asi hasta que alguno sea derrotado.
import random

personajes = ["A", "B"]

ataqueA = random.randint(0,100)
defensaA = random.randint(0,100)
ataqueB = random.randint(0,100)
defensaB = random.randint(0,100)

print(f"Ataque A: {ataqueA}")
print(f"Defensa A: {defensaA}")
print(f"Ataque B: {ataqueB}")
print(f"Defensa B: {defensaB}")

turno = random.choice(personajes)

while(defensaA > 0 and defensaB > 0):
    if turno == "A":
        defensaB -= ataqueA
        print(f"Defensa B: {defensaB}")
        turno = "B"
    else:
        defensaA -= ataqueB
        print(f"Defensa A: {defensaA}")
        turno = "A"

if defensaA > 0:
    print("Gana A")
else:
    print("Gana B")