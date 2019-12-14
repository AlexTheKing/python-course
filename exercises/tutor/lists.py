'''
Есть список с числами. Необходимо составить новый список, причем для каждого элемента этого списка вывести сумму двух его соседей. Для крайних элементов одним из соседей считается элемент с противоположного конца списка.
Например:
[1, 3, 5, 6, 10] -> [13, 6, 9, 15, 7]
'''

a = [1, 3, 5, 6, 10]
b = []

for index in range(len(a)):
	if index == 0:
		value = a[index + 1] + a[-1]
	elif index == len(a) - 1:
		value = a[index - 1] + a[0]
	else:
		value = a[index - 1] + a[index + 1]
	b.append(value)

'''
b = []
for index in range(len(a)):
	previous_index = (index - 1)
	next_index = (index + 1) % len(a)
	value = a[previous_index] + a[next_index]
	b.append(value)
'''

print(b)
