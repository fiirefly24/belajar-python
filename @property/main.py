class Rectangle:
    def __init__(self, width=1, height=1):
        self._width = width
        self._height = height
    
    @property    
    def width(self):
        return f"{self._width:.1f}cm"
    
    @width.setter    
    def width(self, newWidth):
        if newWidth <= 0:
            print("Width must be positive!")
        else:
            self._width = newWidth
            
    @width.deleter
    def width(self):
        print("Deleting Width!")
        del self._width
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
        
    @height.setter    
    def height(self, newHeight):
        if newHeight <= 0:
            print("Width must be positive!")
        else:
            self._height = newHeight
            
    @height.deleter
    def height(self):
        print("Deleting Height!")
        del self._height
    
    def area(self):
        return self._width * self._height

rect = Rectangle()
    
# Use Setter
rect.width = 5
rect.height = 6

# Use Getter
print(f"The current width is {rect.width} and the height is {rect.height}")

# Print Area
print(rect.area())

# Use Deleter
del rect.width 
del rect.height

# Attempt to access deleted attributes
try:
    print(f"The current width is {rect.width} and the height is {rect.height}")
except AttributeError as e:
    print(f"Error: {e}")