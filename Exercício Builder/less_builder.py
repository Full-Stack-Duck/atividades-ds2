from house_builder import HouseBuilder


class LessBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.set_foundation("Less house foundation")

    def build_structure(self):
        self.house.set_structure("Less house structure")

    def build_roof(self):
        self.house.set_roof("Less house roof")

    def build_paint(self):
        self.house.set_paint("Less house paint")