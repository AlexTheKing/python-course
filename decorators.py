def decor(func):
	def decorated():
		print("Inside decor")
		func()
		print("Outside decor")
	return decorated

@decor
def pa():
	print('123')

pa()
