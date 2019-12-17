class Cat:
	def __init__(self, name):
		self.name = name

	def meow(self):
		print('Meow!')

	def drink(self, beverage):
		print('Meow! I drink {}!'.format(beverage))

cat = Cat('Tom')
cat.color = 'black'
print(cat.name)
print(cat.color)
cat.meow()
cat.drink('milk')