class Banco:
    def __init__(self):
        self.__cuentas = []

    @property
    def cuentas(self):
        return self.__cuentas

    def agregar_cuenta(self, numero_cuenta, rut, saldo, movimientos):
        cuenta = {}
        cuenta["numero_cuenta"] = numero_cuenta
        cuenta["rut"] = rut
        cuenta["saldo"] = saldo
        cuenta["movimientos"] = movimientos
        self.cuentas.append(cuenta)
    
    def estado_cuentas(self, cuenta):
        print(f'Estado de la cuenta: {cuenta["numero_cuenta"]}')
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

class Cuenta:
    numero_movimiento = 0

    def __init__(self, numero_cuenta, rut, saldo = 0):
        self.__numero_cuenta = numero_cuenta
        self.__rut = rut   
        self.__saldo = saldo
        self.__movimientos = []

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def rut(self):
        return self.__rut
    
    @property
    def saldo(self):
        return self.__saldo    
    
    @property
    def movimientos(self):
        return self.__movimientos

    def agregar_movimiento(self, tipo_movimiento, fecha_movimiento, monto_movimiento):
        movimiento = {}
        self.numero_movimiento += 1

        if tipo_movimiento == 'cargo':
            self.__saldo -= monto_movimiento
        elif tipo_movimiento == 'abono':
            self.__saldo += monto_movimiento

        movimiento["numero_movimiento"] = self.numero_movimiento
        movimiento["tipo_movimiento"] = tipo_movimiento
        movimiento["fecha_movimiento"] = fecha_movimiento
        movimiento["monto_movimiento"] = monto_movimiento
        movimiento["saldo"] = self.__saldo
        self.__movimientos.append(movimiento)
    
    def estado_cuenta(self):
        print(f'Estado de la cuenta: {self.__numero_cuenta}')
        print(f'Rut: {self.__rut}')
        print(f"{'------- Movimientos -------' : ^100}")
        for m in self.movimientos:
            print(m)


cuenta1 = Cuenta(12345, '1-9', 1000)
cuenta1.agregar_movimiento('abono', '28-04-2023', 1000)
cuenta1.agregar_movimiento('cargo', '28-04-2023', 500)
cuenta2 = Cuenta(54321, '0-8', 2000)
cuenta2.agregar_movimiento('abono', '28-04-2023', 5000)
cuenta2.agregar_movimiento('cargo', '28-04-2023', 500)
cuenta2.agregar_movimiento('abono', '28-04-2023', 10000)
#cuenta1.estado_cuenta()
banco1 = Banco()
banco1.agregar_cuenta(cuenta1.numero_cuenta, cuenta1.rut, cuenta1.saldo, cuenta1.movimientos)
banco1.agregar_cuenta(cuenta2.numero_cuenta, cuenta2.rut, cuenta2.saldo, cuenta2.movimientos)

#banco1.consultar_por_cuenta(12345)
banco1.consultar_por_rut('0-8')

