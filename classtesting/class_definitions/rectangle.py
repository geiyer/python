from .shape import Shape

class Rectangle(Shape):
    def __init__(self, h, b):
        
        self.height = h
        self.base = b

    def area(self):
        return self.height*self.base

    