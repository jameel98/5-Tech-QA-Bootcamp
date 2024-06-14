from week7.inheritance.shape import Shape


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self.height

    def area(self):
        return self._width * self.height / 2
