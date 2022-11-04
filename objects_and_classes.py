import matplotlib.pyplot as plt
# %matplotlib inline  

class Circle(object):
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
        
    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 

class Rectangle(object):
    def __init__(self, color, length, breadth):
        self.color = color
        self.length = length
        self.breadth = breadth
        
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.length, self.breadth ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
Circle_1 = Circle("green", 13)
Circle_1.add_radius(10)
print("The new radius of Circle_1 is", Circle_1.radius)
Circle_1.drawCircle()

Rectangle_1 = Rectangle("orange", 20, 6)
Rectangle_1.drawRectangle()