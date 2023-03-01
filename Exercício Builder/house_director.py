class HouseDirector:
    def __init__(self, house_builder):
        self.house_builder = house_builder

    def construct_house(self):
        self.house_builder.build_foundation()
        self.house_builder.build_structure()
        self.house_builder.build_roof()
        self.house_builder.build_paint()