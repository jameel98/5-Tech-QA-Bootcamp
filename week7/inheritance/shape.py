class Shape:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    def area(self):
        return 0.0

    @color.setter
    def color(self, color):
        self._color = color


