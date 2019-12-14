'''
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
...
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
'''

bottles = 99

while bottles >= 0:
	if bottles == 1:
		print('1 bottle of beer on the wall, 1 bottle of beer.')
		print('Take one down and pass it around, no more bottles of beer on the wall.')
	elif bottles == 0:
		print('No more bottles of beer on the wall, no more bottles of beer.')
		print('Go to the store and buy some more, 99 bottles of beer on the wall.')
	else:
		bottle_string = str(bottles - 1) + (' bottles' if (bottles - 1) > 1 else ' bottle')
		print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
		print(f'Take one down and pass it around, {bottle_string} of beer on the wall.')
	bottles -= 1

'''
a = '{} bottles of beer'.format(bottles)
b = '{ZZZ} bottles of beer'.format(ZZZ=bottles)
c = f'{bottles} bottles of beer'
print(a)
print(b)
print(c)
'''













