#polymorphism
from abc import ABC, abstractmethod

class Shapes:
    @abstractmethod
    def area(self)
        pass


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height


shapes=[Circle(),Triangle(),Rectangle()]
