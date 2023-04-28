class Motocicleta():
    estado = "nueva"
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo = 0):
        self._color = color
        self._matricula = matricula
        self._combustible_litros = combustible_litros
        self._numero_ruedas = numero_ruedas
        self._marca = marca
        self._modelo = modelo
        self._fecha_fabricacion = fecha_fabricacion
        self._velocidad_punta = velocidad_punta
        self._peso = peso
        self._combustible_maximo = combustible_maximo
    
    def arrancar(self):
        if not self.motor:
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha")

    def detener(self):
        if self.motor:
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")

    def consultar_precio(self):
        print(f"El precio de la motocicleta {self._marca} {self._modelo} es de {self.precio}$")       

    def comprobar_deposito(self):
        print(f"--->REPORTE DE DEPÓSITO DE {self._marca} {self._modelo}<---")
        print(f"El depósito tiene {self._combustible_litros} litros.")
        print(f"La capacidad máxima del tanque de combustible es de {self._combustible_maximo}.")
        print(f"Faltan {self._combustible_maximo - self._combustible_litros} litros para llenar el depósito.")
        print(f"--->FIN DEL REPORTE<---\n")

    def repostar(self):
        while True:
            try:
                cantidad = float(input("Ingrese la cantidad de litros a repostar: "))
                capacidad = self._combustible_maximo - self._combustible_litros
                if (cantidad > capacidad):
                    print(f"El máximo a repostar es de {capacidad} litros. Inténtalo nuevamente.")
                else:
                    self._combustible_litros += cantidad
                    print("Repostaje exitoso")
                    print(f"El depósito tiene {self._combustible_litros} litros.")
                    break
            except ValueError:
                print("Ingrese un valor numérico.")

moto1 = Motocicleta("negro", "XX1234", 10, 2, "Honda",
                    "Modelo Honda", 2019, 100, 80)
print(vars(moto1))
moto2 = Motocicleta(color="blanco", matricula="XX1234", combustible_litros=0, numero_ruedas=2,
                    marca="Honda", modelo="Modelo Honda", fecha_fabricacion=2019, velocidad_punta=100, peso=80)
print(vars(moto2))

moto1.arrancar()
moto1.detener()

moto1.precio = 9000
print(f"El precio de la motocicleta {moto1._marca} {moto1._modelo} es de {moto1.precio}$")

moto1._combustible_maximo = 17
moto2._combustible_maximo = 20

moto1.repostar()
print(vars(moto1))
