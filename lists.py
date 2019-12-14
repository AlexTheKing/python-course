# Запустить это - python lists.py

# Списки
list_of_numbers = [1, 2, 3]
list_of_strings = ["Hello", " ", "World", "!"]
list_of_mixed_types = [1, "apple", 2, 4.5, False]

print(type(list_of_numbers))

a_list = list()

print("List of numbers:", list_of_numbers)
print("List of strings:", list_of_strings)
print("List of mixed types:", list_of_mixed_types)

# Индексация
# Начинается с 0
# список	[45, 12, 32, 95]
# элементы	  0   1   2   3
hello = list_of_strings[0]  # начинается с 0
four_and_a_half = list_of_mixed_types[3]  # это четвертый элемент списка
print("First element of list of strings:", hello)
print("Fourth element of list of mixed types:", four_and_a_half)

# Количество элементов, len() - универсальная функция подсчета количества элементов списка
count_strings = len(list_of_strings)
print("Length of list of strings:", count_strings)

# Строки - те же списки символов
print("Length of hello:", len(hello))
print("Third letter of hello:", hello[2])
