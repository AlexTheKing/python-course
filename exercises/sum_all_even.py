'''
Суммировать все четные числа от 0 до n
'''

n = int(input('Enter number: '))
counter = 0
accumulator = 0

while counter != n:
	if counter % 2 == 0:
		accumulator += counter
	counter += 1  # counter = counter + 1

print(accumulator)