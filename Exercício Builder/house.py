class House:
    def __init__(self):
        self.__foundation = None
        self.__structure = None
        self.__roof = None
        self.__paint = None

    def set_foundation(self, foundation):
        self.__foundation = foundation

    def set_structure(self, structure):
        self.__structure = structure

    def set_roof(self, roof):
        self.__roof = roof

    def set_paint(self, paint):
        self.__paint = paint

    def get_house(self):
        return f"Foundation: {self.__foundation}, Structure: {self.__structure}, Roof: {self.__roof}, Paint: {self.__paint}"