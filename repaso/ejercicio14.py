pizza_veg = ["Pimiento", "Tofu"]
pizza_nor = ["Pepperoni", "Jamón", "Salmón"]
base_pizza = ["Tomate", "Mozarella"]

print("- Vegetariana")
print("- No-Vegetariana")
tipo_pizza = input("Escoja el tipo de pizza: ")

if tipo_pizza.upper() == 'VEGETARIANA':
    for ingredientes in pizza_veg:
        print(f"- {ingredientes}")
    ingrediente = input("Escoja un ingrediente: ")
else:
    for ingredientes in pizza_nor:
        print(f"- {ingredientes}")
    ingrediente = input("Escoja un ingrediente: ")

print("Detalle de la pizza seleccionada: ")
print(f"Tipo de pizza: {tipo_pizza}")
print("\nIngredientes: ")
base_pizza.append(ingrediente.capitalize())
for index, ingredientes in enumerate(base_pizza, start=1):
    print(f"{index}. {ingredientes}")