# Write a Python class named Circle 
# constructed by a radius and two methods 
# which will compute the area and the perimeter of a circle.
import math
class Circle:
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        return math.pi * radius ** 2

    def perimeter(self) -> float:
        return  2 * math.pi * radius

