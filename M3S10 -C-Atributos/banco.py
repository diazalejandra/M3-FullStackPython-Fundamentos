import datetime

class Banco:
    cuentas = []
    
    # parte así la Lista
        # 'nombre_titular': _nombre_titular,
        # 'cuenta_rut': _cuenta_rut,
        # 'balance': 0,
        # 'movimientos': [] 
    
    # Así se vería la lista, después de dos movimientos, asociados a un mismo rut
        #'nombre_titular': 'Carlos Azócar',
        # 'cuenta_rut': '18.387.589',
        # 'balance': 0,
        # 'movimientos': [{'id': 1 ,'tipo': 'abonar': _monto: 3000,'fecha': '2023-04-29 01:30:42','saldo': 4000} , {'id': 2 ,'tipo': 'cargar': _monto: 5000,'fecha': '2023-04-29 01:20:42','saldo': 5000}]
    
    def __init__(self):
        pass

    @classmethod
    def registrar_cuenta(cls, _nombre_titular, _cuenta_rut):
        cuenta = {
            'nombre_titular': _nombre_titular,
            'cuenta_rut': _cuenta_rut,
            'balance': 0,
            'movimientos': [] 
        }
        cls.cuentas.append(cuenta)
        print(f'Usuario {_nombre_titular}, cuenta: {_cuenta_rut}, agregado con éxito')
        
        
    @classmethod
    def agregar_movimiento(cls, _cuenta_rut, _tipo, _monto):
        for cuenta in cls.cuentas:
            if cuenta['cuenta_rut'] == _cuenta_rut:
                if _tipo == 'abonar':
                    cuenta['balance'] += _monto
                    movimiento = {
                        'id': len(cuenta['movimientos']) + 1,
                        'tipo': _tipo,
                        'monto': _monto,
                        'fecha': datetime.datetime.now(),
                        'saldo': cuenta['balance']
                    }
                    cuenta['movimientos'].append(movimiento)
                elif _tipo == 'cargar':
                    if cuenta['balance'] >= _monto:
                        cuenta['balance'] -= _monto
                        movimiento = {
                            'id': len(cuenta['movimientos']) + 1,
                            'tipo': _tipo,
                            'monto': _monto,
                            'fecha': datetime.datetime.now(),
                            'saldo': cuenta['balance']
                        }
                        cuenta['movimientos'].append(movimiento)
                    else:
                        print('No tienes suficiente saldo para realizar esta operación')
                        return
                else:
                    print('Tipo de movimiento no válido')
                    return
                print('Movimiento realizado con éxito')
                print('Saldo actual:', cuenta['balance'])
                return
        print(f'La cuenta con RUT {_cuenta_rut} no existe')

        
    @classmethod
    def ver_estado_cuenta(cls, _cuenta_rut):
        for cuenta in cls.cuentas:
            if cuenta['cuenta_rut'] == _cuenta_rut:
                print('Los datos son: ')
                print('Nombre titular:', cuenta['nombre_titular'])
                print('RUT:', cuenta['cuenta_rut'])
                print('Saldo:', cuenta['balance'])
                print('Movimientos:')
                for movimiento in cuenta['movimientos']:
                    print('- ID:', movimiento['id'])
                    print('  Tipo:', movimiento['tipo'])
                    print('  Monto:', movimiento['monto'])
                    print('  Fecha:', movimiento['fecha'])
                    print('  Saldo después del movimiento:', movimiento['saldo'])
                return
        print(f'La cuenta con RUT {_cuenta_rut} no existe')

print('\n')
Banco.registrar_cuenta('Carlos Azócar','18.387.589')

print('\n')

Banco.registrar_cuenta('Catalina Gómez','17.685.709')

print('\n')
print('Ver estado de cuenta cuenta 1')
Banco.ver_estado_cuenta('18.387.589')

print('\n')

print('Ver estado de cuenta cuenta 2')
Banco.ver_estado_cuenta('17.685.709')


print('\n')
print('Abono dinero a cuenta 1')
Banco.agregar_movimiento('18.387.589','abonar',10)


print('\n')
print('Abono dinero a cuenta 2')
Banco.agregar_movimiento('17.685.709','abonar',5)

print('\n')

print('Ver estado de cuenta cuenta 1')
Banco.ver_estado_cuenta('18.387.589')

print('\n')
print('Agrego un cargo de 5 a la cuenta 1')
Banco.agregar_movimiento('18.387.589','cargar',5)

print('\n')

Banco.ver_estado_cuenta('18.387.589')


print('\n')

Banco.ver_estado_cuenta('17.685.709')
