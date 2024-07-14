class Item:
    def __init__(self, name, final_price, color):
        self._name = name
        self._final_price = final_price
        self._color = color

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for final_price
    @property
    def final_price(self):
        return self._final_price

    # Setter for final_price
    @final_price.setter
    def final_price(self, value):
        self._final_price = value

    # Getter for color
    @property
    def color(self):
        return self._color

    # Setter for color
    @color.setter
    def color(self, value):
        self._color = value
