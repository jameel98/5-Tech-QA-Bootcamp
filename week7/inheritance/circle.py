import math

from week7.inheritance.shape import Shape


class Circle(Shape):
    
    def __init__(self, color, radios):
        super().__init__(color)
        self._radios = radios

    @property
    def radios(self):
        return self._radios

    def area(self):
        return self.radios * self.radios * math.pi

