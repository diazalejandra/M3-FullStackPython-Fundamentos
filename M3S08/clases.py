class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


gato = Animal("Lucas", "gato")
print(vars(gato))

gato.name = "Bruno"
print(vars(gato))

print("\n ---------------")

class Droid:
    def __init__(self, name):
        self.hidden_name = name
        
    @property
    def name(self) -> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid("Arthur")
print(android.name)
android.name = "Citripio"
print(android.name)

android.hidden_name = "Rojo"
print(android.hidden_name)
print(android.name)

print("\n ---------------")
class CalculatedValue:
    def __init__(self, name, height):
        self._name = name
        self._height = height
    
    @property
    def get_calculated_value(self) -> float:
        return 0.35 * self._height

valuex = CalculatedValue("ratio", 10)
print(f'El {valuex._name} es {valuex.get_calculated_value}')

print("\n ---------------")
class Dog():
    obeys_owner = True
    
    def __init__(self, name):
        self._name = name

dog_one = Dog("Robin")
dog_two = Dog("Malta")
dog_three = Dog("Luz")

dog_one.obeys_owner = False
Dog.obeys_owner = False
print(f'{dog_one._name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two._name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three._name} obedece a su dueño {dog_three.obeys_owner}')

print("\n ---------------")
del dog_one.obeys_owner
Dog.obeys_owner = True
print(f'{dog_one._name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two._name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three._name} obedece a su dueño {dog_three.obeys_owner}')