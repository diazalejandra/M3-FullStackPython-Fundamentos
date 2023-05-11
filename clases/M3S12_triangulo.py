altura = int(input("Ingrese la altura del triangulo "))

triangulo = ""
for ele in range(altura):
    triangulo = "*"+triangulo
    print(triangulo)

for ele in range(altura):
    print("*"*(ele+1))


#Escriba un programa que almacene una contraseña en una variable, pregunta al usuario por la contraseña hasta que introduzca la correcta.

contrasena = "abcd1."

while True:
    ingreso = input("Ingrese su contraseña: ")
    if ingreso == contrasena:
        print("Pase usted")
        break
    else:
        print("Contraseña incorrecta")

