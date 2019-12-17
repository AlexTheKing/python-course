'''
Найти все числа от 1 до 1000, которые содержат цифру 3
'''

#235 -> '235' -> ['2', '3', '5']

a = [number for number in range(1000) if '3' in str(number)]
print(a)