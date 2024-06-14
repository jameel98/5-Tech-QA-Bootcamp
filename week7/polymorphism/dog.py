from week7.polymorphism.animal import Animal


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
