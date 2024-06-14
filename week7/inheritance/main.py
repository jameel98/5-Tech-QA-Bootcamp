from week7.inheritance.circle import Circle
from week7.inheritance.rectangle import Rectangle
from week7.inheritance.shape import Shape

if __name__ == '__main__':
    shape = Shape("red")
    rectangle = Rectangle("red", 12, 10)
    circle = Circle("blue", 5)

    print(shape.area())
    print(rectangle.area())
    print(circle.area())


