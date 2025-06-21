import math

class Shape:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area():
    raise NotImplementedError

class Rectangle(Shape):  
  def area(self):
    return self.length * self.width

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    self.pie = math.pi

  def area(self):
    return self.pie * (self.radius ** 2)