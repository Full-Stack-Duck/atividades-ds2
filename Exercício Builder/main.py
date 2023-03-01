from house_director import HouseDirector
from complex_house_builder import ComplexHouseBuilder
from less_builder import LessBuilder

less_builder = LessBuilder()
complex_house_builder = ComplexHouseBuilder()

house_director = HouseDirector(less_builder)
house_director.construct_house()

simple_house = less_builder.house
print(simple_house.get_house())

house_director = HouseDirector(complex_house_builder)
house_director.construct_house()

complex_house = complex_house_builder.house
print(complex_house.get_house())