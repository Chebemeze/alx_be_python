import math

class Shape:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def area():
    raise NotImplementedError

class Rectangle(Shape):  
  def area(self):
    return self.a * self.b

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    self.pie = math.pi

  def area(self):
    return self.pie * pow(self.radius, 2)

# pie = math.pi
# a = pie * pow(3, 2)
# print(a)