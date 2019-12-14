# Запустить это - python for.py

# Списки
list_of_numbers = [1, 2, 3]
list_of_strings = ["Hello", " ", "World", "!"]
list_of_mixed_types = [1, "apple", 2, 4.5, False]

# Вывести элементы списка
print("Elements of list of mixed types:")
for element in list_of_mixed_types:
    print(element)

# Сложить все числа в списке
print("Sum of all numbers in list of numbers:")
accumulator = 0
for element in list_of_numbers:
    accumulator += element
print(accumulator)

# Конкатенировать все строки в списке
print("Concatenate all strings in list of strings:")
accumulator = ""
for element in list_of_strings:
    accumulator += element
print(accumulator)

# Как я говорил, строки = списки символов
print("Letters:")
for letter in "Alex":
	print(letter)