#Escriba un programa que elimine un signo de exclamación del final de una cadena. 
#Puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

entrada = input("Ingrese un texto: ")

print(''.join(entrada.rsplit('!', 1)))

##Otra opción
print(entrada[:-1] if entrada[-1] == "!" else entrada)