class Person:
	def say_hi(self):
		print('Hello!')

class Student(Person):
	def say_hi(self):
		print('Hello, I am student!')

person = Person()
student = Student()
person_list = [Person(), Student(), Person(), Student()]
for person in person_list:
	person.say_hi()