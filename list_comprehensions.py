# Запустить это - python list_generators.py

# Списочные выражения - способ построить список из другой последовательности
name = "Alex"
triple_name = [letter * 3 for letter in name]
print("Tttrrriiipppllleee name:", name, "=", triple_name)

temp = []
for letter in name:
	temp.append(letter * 3)

# В выражении можно использовать и условия
# Удвоить каждую букву, кроме "e"
name = 'Alex'
double_name_except_e = [
	letter * 2
	for letter in name
	if letter != "e"
]
print("Double name except 'e':", name, "=", double_name_except_e)

temp = []
for letter in name:
	if letter != 'e':
		temp.append(letter * 3)