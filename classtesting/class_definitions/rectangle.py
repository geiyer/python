from .shape import Shape
from .invalid_side_exception import InvalidSideError

class Rectangle(Shape):
    def __init__(self, h, b):
        if(h < 0 or b < 0): 
            raise InvalidSideError

        self.height = h
        self.base = b

    def area(self):
        return self.height*self.base

    