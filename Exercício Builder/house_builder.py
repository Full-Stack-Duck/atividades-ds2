from abc import ABC, abstractmethod
from house import House


class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @property
    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_paint(self):
        pass