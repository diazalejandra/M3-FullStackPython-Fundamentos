class Artefacto:
    def __init__(self, name, type, owner):
        self.__name = name
        self.__type = type
        self.__owner = owner

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type
    
    @type.setter
    def type(self, type:str) -> None:
        self.__type = type

    @property
    def owner(self) -> str:
        return self.__owner
    
    @owner.setter
    def owner(self, owner:str) -> None:
        self.__owner = owner

artefacto1 = Artefacto("Pinza", "herramienta", "Ale")

print(artefacto1.name)

    