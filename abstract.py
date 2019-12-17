from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area():
		pass

class Square(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

square = Square(2, 3)
print('Area: {0}'.format(square.area()))

shape = Shape()