# Запустить это - python dicts_sets_tuples.py

# Словари
phone_book = {
	"Alex": "+375291994949",
	"John": "+375448484848",
	"Jane": "+375958492123"
}

interests = {
	"Alex": ["Python", "Databases", "Movies with Jason Statham"],
	"John": ["Books", "Star Wars"],
	"Jane": ["Music", "Dancing", "Books", "Movies with Brad Pitt"]
}
print("Phone book:", phone_book)
print("Interests:", interests)

# Индексация
print("My number is:", phone_book["Alex"])
print("My second interest is:", interests["Alex"][1])

# Добавление элементов в словарь
phone_book["Frank"] = "+375129483923"
phone_book["Alex"] = "+375129483923"
interests["Frank"] = []
print("Added new elements to dicts")
print(phone_book)
print(interests)

# Выражения словарей
words = ["Fire", "Water", "Earth", "Air"]
words_length = {word: len(word) for word in words}
print("Words:", words)
print("Words with their length:", words_length)

# Tuples
simple_tuple = ('Jonathan', '+375297184848')
name_phone_tuples = [(name, phone) for (name, phone) in phone_book.items()]
name_phone_tuples = list(phone_book.items())
print(name_phone_tuples)

# Hey, that's wrong!
a = 'I am in variable B'
b = 'I am in variable A'
print(a, b)

# Let's change it. Now it's right!
a, b = b, a
print(a, b)

# Итерация по словарю items() - функция возвращающая пары (ключ, значение)
for key, value in phone_book.items():
	print(key.upper()[::-1], value[::-1])

# Sets
phone_numbers = set()
phone_numbers.add('+375298465797')  # equal to...
phone_numbers.add('+375449345681')
phone_numbers.add('+375298465797')  # ...this
print(phone_numbers)  # only 2 elements	

# Set comprehension
my_interests = set(interests["Alex"])
john_jane_interests = {
	interest
	for interest_list in interests.values()
	for interest in interest_list
}
print(john_jane_interests)

# Operations on sets
print(john_jane_interests & my_interests)  # intersection
print(john_jane_interests | my_interests)  # union
print(john_jane_interests - my_interests)  # difference
print(john_jane_interests ^ my_interests)  # symmetric difference


# Complex
rows = [1, 2, 3, 4]
cols = ['a', 'b', 'c', 'd']

dictionary = {
	(col, row): col + str(row)
	for col in cols if len(col) == 1
	for row in rows if row > 0
}
print(dictionary)
print(dictionary['b', 3])
print(dictionary[('b', 3)])

# Generators
a_generator = (i**2 for i in range(100000000000000000000000000000000))
print(a_generator)
print(list(a_generator))