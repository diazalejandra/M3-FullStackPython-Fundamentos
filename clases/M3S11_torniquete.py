# se necesita realizar un programa basado en clases que permita automatizar el torniquete (control de acceso)
# de una micro, de la siguiente manera

# 1. Las personas que aboradan la micro son, mujeres, hombres, niños y aduto mayor, de los cuales los niños no pagan 
#    y los adultos mayores pagan la tarifa el 50%

# 2 el cobro actual de la micro es de 730 pesos

# 3 por lo que necesitamos un reporte de operacion por dia donde, por micro (cada micro se reguistra por patente), 
#   se listen los tipos de usuario y la cantidad total recaudad por cada, anexar a este reporte el total por dia

# 4. seria interesante que apart6e del reporte anterior que estotal, tener uno filtrado por dia y otro filtrado por persona
from datetime import datetime

class Operacion:
    fecha_hoy = datetime.today().strftime('%d-%m-%Y')
    valor_pasaje = 730
    tipo_persona = {"mujer": 1, "hombre": 1, "niño": 0, "adulto_mayor": 0.5 }

    def __init__(self):
        self.micros = []
        self.pasajes = []
    
    def agregar_micro(self, patente):
        self.micros.append(patente)
        print("Se agregó correctamente la micro")

    def agregar_pasaje(self, patente_micro, tipo_persona, fecha):
        if tipo_persona not in self.tipo_persona:
            print("Tipo de persona no válida.")
        else:
            micro = list(filter(lambda e: e == patente_micro, self.micros))
            if micro is not None:
                self.pasajes.append({
                    "patente_micro": patente_micro,
                    "tipo_persona": tipo_persona,
                    "valor": int(self.tipo_persona[tipo_persona]*self.valor_pasaje),
                    "fecha": fecha
                })
            else:
                print(f"Micro {patente_micro} no registrada")
    
    def operacion_diaria(self):
        print(f"\n----- Operación Diaria -----")
        for micro in self.micros:
            total_diario = 0
            total_nino = 0
            total_mujer = 0
            total_hombre = 0
            total_mayor = 0

            print(f"\nPatente: {micro}")
            pasajes = list(filter(lambda e: (e['patente_micro'] == micro and e["fecha"] == self.fecha_hoy), self.pasajes))
            for pasaje in pasajes:
                total_diario += pasaje["valor"]
                if pasaje["tipo_persona"] == "mujer":
                    total_mujer += pasaje["valor"]
                elif pasaje["tipo_persona"] == "hombre":
                    total_hombre += pasaje["valor"]
                elif pasaje["tipo_persona"] == "niño":
                    total_nino += pasaje["valor"]
                elif pasaje["tipo_persona"] == "adulto_mayor":
                    total_mayor += pasaje["valor"]

            
            print(f"Fecha: {self.fecha_hoy}")
            print(f"Total recaudado: {total_diario}")
            print(f"- Mujer: {total_mujer}")
            print(f"- Hombre: {total_hombre}")
            print(f"- Niño: {total_nino}")
            print(f"- Adulto Mayor: {total_mayor}")
            print(f"\n--------- Pasajes ---------")
            for pasaje in pasajes:
                print(f"{pasaje}\r")

    def operacion_por_fecha(self, fecha_operacion):
        print(f"\n----- Operación por Fecha -----")
        for micro in self.micros:
            total_diario = 0
            total_nino = 0
            total_mujer = 0
            total_hombre = 0
            total_mayor = 0
            
            pasajes = list(filter(lambda e: (e['patente_micro'] == micro and e["fecha"] == fecha_operacion), self.pasajes))

            if len(pasajes) != 0:
                for pasaje in pasajes:
                    total_diario += pasaje["valor"]
                    if pasaje["tipo_persona"] == "mujer":
                        total_mujer += pasaje["valor"]
                    elif pasaje["tipo_persona"] == "hombre":
                        total_hombre += pasaje["valor"]
                    elif pasaje["tipo_persona"] == "niño":
                        total_nino += pasaje["valor"]
                    elif pasaje["tipo_persona"] == "adulto_mayor":
                        total_mayor += pasaje["valor"]
                
                print(f"\nPatente: {micro}")
                print(f"Fecha: {fecha_operacion}")
                print(f"Total recaudado: {total_diario}")
                print(f"- Mujer: {total_mujer}")
                print(f"- Hombre: {total_hombre}")
                print(f"- Niño: {total_nino}")
                print(f"- Adulto Mayor: {total_mayor}")
                print(f"\n--------- Pasajes ---------")
                for pasaje in pasajes:
                    print(f"{pasaje}\r")

    def operacion_por_pasajero(self, tipo_persona):
        print(f"\n----- Operación por Pasajero -----")
        for micro in self.micros:
            total_diario = 0

            pasajes = list(filter(lambda e: (e['patente_micro'] == micro and e["tipo_persona"] == tipo_persona), self.pasajes))
            for pasaje in pasajes:
                total_diario += pasaje["valor"]
                
            print(f"\nPatente: {micro}")
            print(f"Fecha: {self.fecha_hoy}")
            print(f"Total recaudado: {total_diario}")
            print(f"\n--------- Pasajes ---------")
            for pasaje in pasajes:
                print(f"{pasaje}\r")

operacion = Operacion()
operacion.agregar_micro('ASD1234')
operacion.agregar_pasaje('ASD1234', "niño", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "niño", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "niño", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "mujer", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "mujer", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "hombre", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "hombre", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "hombre", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "hombre", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "hombre", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_pasaje('ASD1234', "adulto_mayor", "02-05-2023")
operacion.agregar_micro('ASD1235')
operacion.agregar_pasaje('ASD1235', "niño", "02-05-2023")
operacion.agregar_pasaje('ASD1235', "niño", "02-05-2023")
operacion.agregar_pasaje('ASD1235', "mujer", "02-05-2023")
operacion.agregar_pasaje('ASD1235', "mujer", "02-05-2023")
operacion.agregar_pasaje('ASD1235', "hombre", "02-05-2023")
operacion.agregar_pasaje('ASD1235', "adulto_mayor", "01-05-2023")
#operacion.operacion_diaria()
operacion.operacion_por_fecha("01-05-2023")
#operacion.operacion_por_pasajero("mujer")