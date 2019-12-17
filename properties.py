class Car:
	DEFAULT_COLOR = 'orange'

	def __init__(self, model, color=DEFAULT_COLOR):
		self.__model = model
		self.__color = color

	# Color
	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	@color.deleter
	def color(self):
		self.__color = Car.DEFAULT_COLOR

	# Model
	@property
	def model(self):
		return self.__model

	@model.setter
	def model(self, value):
		# Запрещаем изменение модели после создания
		pass

	@model.deleter
	def model(self):
		# Запрещаем удаление модели после создания
		pass

car = Car('Audi', 'red')

print('Get color:', car.color)
car.color = 'black'
print('Set color:', car.color)
del car.color
print('Delete color:', car.color)

print('Get model:', car.model)
car.model = 'Ford'
print('Set model:', car.model)
del car.model
print('Delete model:', car.model)



