# Запустить это - python boolean.py

apples = 2
bananas = 4
print("Apples:", apples)
print("Bananas:", bananas)

# Считаем количество фруктов
fruits = apples + bananas
print("Fruits:", fruits)

# Фруктов больше 5?
is_greater_than_five = (fruits > 5)
print("Is greater than 5:", is_greater_than_five)

# Фруктов больше 8?
is_greater_than_eight = (fruits > 8)
print("Is greater than 8:", is_greater_than_eight)

# Boolean = True или False (истина или ложь, да или нет)

# Остальные операции над boolean
x = 2
y = 5
print("x:", x)
print("y:", y)
print("x < 2", x < 2)
print("x <= 2", x <= 2)
print("y > 5", y > 5)
print("y >= 5", y >= 5)
print("x == 2", x == 2)
print("y != 6", y != 6) 

# Операция AND
my_name = "Alex"
my_age = 21
print("Me:", my_name, my_age)

name = "Max"
age = 24
print("Someone:", name, age)

is_me = name == my_name and age == my_age
print("Is it me:", is_me)

# X and Y = RESULT
# T and T     T
# T and F     F
# F and T     F
# F and F     F

# Операция OR
color = "red"
print("Color:", color)

is_blue_or_red = color == "blue" or color == "red"
print("Is blue or red:", is_blue_or_red)

# X or Y = RESULT
# T or T =   T
# T or F =   T
# F or T =   T
# F or F =   F

# Операция NOT
true_value = True
false_value = not true_value
print("True value:", true_value)
print("False value:", false_value)

# not X = RESULT
# not T =   F
# not F =   T
