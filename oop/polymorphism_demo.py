import math 

class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__()
        self.length: int = length
        self.width: int = width
    
    def area(self):
        area = self.length * self.width
        return area
    
class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__()
        self.radius: int = radius

    def area(self):
        area = math.pi * (self.radius * self.radius)
        return area