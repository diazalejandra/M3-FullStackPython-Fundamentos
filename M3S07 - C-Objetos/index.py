class Transporte:
    pass

transporte1 = Transporte()
transporte2 = Transporte()

class BuzzLightYear:
    pass

buzz1 = BuzzLightYear()
buzz2 = BuzzLightYear()

print(type(transporte1))
print(type(buzz1))

class Droid:
    def __init__(self):
        self.power_on = True

    def switch_on(self):
        print("Hola, soy un droid y estoy a tu orden")
        self.power_on = True

    def switch_off(self):
        print("Adios, enciendeme cuando me necesites")
        self.power_on = False

k8_arthur = Droid()
k8_citripio = Droid()

print(f"Power on Arthur: {k8_arthur.power_on}")

k8_citripio.switch_off()
print(f"Power on Citripio: {k8_citripio.power_on}")

k8_arthur.switch_off()
print(f"Power on Arthur: {k8_arthur.power_on}")

class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)