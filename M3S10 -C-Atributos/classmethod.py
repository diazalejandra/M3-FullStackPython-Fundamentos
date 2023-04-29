class Empleado:
    sueldo_base = 100000

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @classmethod
    def get_sueldo_base(cls):
        return cls.sueldo_base

    @classmethod
    def set_sueldo_base(cls, sueldo):
        cls.sueldo_base = sueldo

