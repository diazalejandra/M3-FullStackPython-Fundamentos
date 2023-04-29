from datetime import datetime
class Banco:
    fecha = datetime.today().strftime('%Y-%m-%d')
    
    def __init__(self):
        self.__cuentas = []

    @property
    def cuentas(self):
        return self.__cuentas
    
    def crear_cuenta(self, numero_cuenta, rut, saldo = 0):
        cuenta = {}
        cuenta["numero_cuenta"] = numero_cuenta
        cuenta["rut"] = rut
        cuenta["saldo"] = saldo
        cuenta["numero_movimiento"] = 0
        cuenta["movimientos"] = []
        self.cuentas.append(cuenta)
        print(f"Cuenta creada exitosamente.")
            
    
    def agregar_movimiento(self, numero_cuenta, tipo_movimiento, fecha_movimiento, monto_movimiento):
        movimiento = {}

        for c in self.cuentas:
            if c["numero_cuenta"] == numero_cuenta:
                c["numero_movimiento"] += 1

                if tipo_movimiento == 'cargo':
                    c["saldo"] -= monto_movimiento
                elif tipo_movimiento == 'abono':
                    c["saldo"] += monto_movimiento

                movimiento["numero_movimiento"] = c["numero_movimiento"]
                movimiento["tipo_movimiento"] = tipo_movimiento
                movimiento["fecha_movimiento"] = fecha_movimiento
                movimiento["monto_movimiento"] = monto_movimiento
                movimiento["saldo"] = c["saldo"]

                c["movimientos"].append(movimiento)
                print(f"Movimiento creado exitosamente.")

    def estado_cuentas(self, cuenta):
        print(f'\nEstado de la cuenta: {cuenta["numero_cuenta"]}')
        print(f'Rut: {cuenta["rut"]}')
        print(f'Saldo: {cuenta["saldo"]}')
        print(f"{'------- Movimientos -------' : ^100}")
        for m in cuenta["movimientos"]:
            print(m)
    
    def consultar_por_cuenta(self, numero_cuenta):
        no_existe = True
        for c in self.cuentas:
            if c["numero_cuenta"] == numero_cuenta:
                no_existe = False
                self.estado_cuentas(c)
        if(no_existe):
            print(f"La cuenta {numero_cuenta} no existe en este banco.")

    def consultar_por_rut(self, numero_rut):
        no_existe = True
        for c in self.cuentas:
            if c["rut"] == numero_rut:
                no_existe = False
                self.estado_cuentas(c)
        if(no_existe):
            print(f"El rut {numero_rut} no tiene cuenta en este banco.")

def imprimir_menu():
    #banco1 = Banco()
    print(f"Bienvenido al Banco de Ale")
    print(f"-------- Menú --------")
    print(f"1. Consultar movimientos por cuenta")
    print(f"2. Consultar movimientos por rut")
    print(f"3. Realizar un movimiento")
    print(f"4. Crear una cuenta")
    print(f"5. Salir")
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            match opcion:
                case 1:
                    cuenta = int(input("Indique el número de la cuenta a consultar: "))
                    banco1.consultar_por_cuenta(cuenta)
                case 2:
                    rut = input("Indique el rut a consultar: ")
                    banco1.consultar_por_rut(rut)
                case 3:
                    cuenta = int(input("Indique la cuenta: "))
                    movimiento = input("Indique el movimiento a realizar (abono o cargo): ")
                    monto = int(input("Ingrese el monto: "))
                    banco1.agregar_movimiento(cuenta, movimiento, banco1.fecha, monto)
                case 4:
                    cuenta = int(input("Ingrese el número de cuenta: "))
                    rut = input("Ingrese su rut: ")
                    banco1.crear_cuenta(cuenta, rut)
                case 5:
                    break
        except ValueError:
            print("Ingrese un número válido")

banco1 = Banco()
banco1.crear_cuenta(12345, '1-9')
banco1.crear_cuenta(54321, '0-8')
banco1.agregar_movimiento(12345, 'abono', '28-04-2023', 1000)
banco1.agregar_movimiento(12345, 'cargo', '28-04-2023', 10)

banco1.consultar_por_cuenta(12345)
#banco1.consultar_por_rut('1-9')

imprimir_menu()

