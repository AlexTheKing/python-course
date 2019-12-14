'''
Есть список с числами. Необходимо составить новый список, причем для каждого элемента этого списка вывести сумму двух его соседей.
Для крайних элементов одним из соседей считается элемент с противоположного конца списка.
Например:
[1, 3, 5, 6, 10] -> [13, 6, 9, 15, 7]
'''

l = [1, 3, 5, 6, 10]
a = []

a.append(l[1] + l[-1])

for index in range(1, len(l) - 1):
	a.append(l[index - 1] + l[index + 1])

a.append(l[0] + l[-2])

print(a)