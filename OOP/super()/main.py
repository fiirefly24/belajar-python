
class Shape:
    def __init__(self, color, is_filled):
        self._color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self._color} and {'filled' if self.is_filled == True else "Not Filled"}")
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius**2}cm^2 and", end=" ")
        super().describe()
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

        
circle = Circle("Red", True, 5)
square = Square("Green", True, 12)
triangle = Triangle("Yellow", True, 12, 20)

circle.describe()