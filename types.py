# Запустить это - types.py

# Число
age = 15
print("Age:", age)
print("Is age higher than 10?", age > 10)

# Строка
password_code = "16486"
print("Password code:", password_code)
print("Length of password:", len(password_code))

# Число в строку
# print("Age " + age) - выдаст ошибку, нельзя сложить строку с числом
print("Age: " + str(age))  # str - сокращение от string (строка)

# Строку в число
age = int(input("How old are you? "))  # int - сокращение от integer - целое число
print("Is age even?", age % 2 == 0)

# Другие преобразования
boolean_value = bool("True")  # "True" или "False"
float_value = float("4.5")  # float - число с плавающей точкой

# Вывести тип
print(123, type(123))
print("123", type("123"))
print(True, type(True))
print("True", type("True"))
print(4.5, type(4.5))
print("4.5", type("4.5"))

