class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello! My name is {0}'.format(self.name))

class Student(Person):
	def __init__(self, name, university):
		super(Student, self).__init__(name)
		self.university = university

	def say_hi(self):
		super(Student, self).say_hi()
		print('I am student of {0}!'.format(self.university))
		print('I love my name <3 - {0}'.format(self.name))
		

person = Person('John')
person.say_hi()
student = Student('Jane', 'MIT')
student.say_hi()