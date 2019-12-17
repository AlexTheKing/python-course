class Car:
	def __init__(self, model):
		self.model = model
		self.__max_speed = 240
		self.__started = False

	def start(self):
		self.__started = True
		self.__update_software()
		print('Wroom wroom')

	def accelerate(self, speed):
		if self.__started:
			car_speed = self.__max_speed if speed > self.__max_speed else speed
			print('Getting up to {0} km/h!'.format(car_speed))
		else:
			print('I am not started!')

	def stop(self):
		self.__started = False
		print('Stopped')

	def __update_software(self):
		print('Checking software updates')

car = Car('Audi')
print(car.model)

try:
	print(car.__max_speed)
except AttributeError:
	print("Cannot access car's max speed!")

car.start()

try:
	print(car.__update_software())
except AttributeError:
	print("Cannot access update software method!")

car.accelerate(60)
car.accelerate(250)
car.stop()