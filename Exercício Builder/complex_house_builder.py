from house_builder import HouseBuilder


class ComplexHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.set_foundation("Complex foundation")

    def build_structure(self):
        self.house.set_structure("Complex structure")

    def build_roof(self):
        self.house.set_roof("Complex roof")

    def build_paint(self):
        self.house.set_paint("Complex paint")