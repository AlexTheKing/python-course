# Запустить это - python functions.py

# Так выглядит объявление именнованой функции
# def - ключевое слово
# add - имя функции
# x, y - параметры
def add(x, y):
	print("Function add() is invoked!")
	return x + y  # ключевое слово return означает, что функция вернет значение x + y

print("add(1, 2) =", add(1, 2))
print("add(4, 3) =", add(4, 3))
print("add(-2, 2) =", add(-2, 2))
print('add("Hello", " world!") =', add("Hello", " world!"))


# Так выглядит объявление анонимной функции. Они должны быть однострочными и поэтому ей не нужен return - вычисленное значение возвращается автоматически
func = lambda x: x ** 2
print("func(2) =", func(2))
print("(lambda x: x ** 3)(4) =", (lambda x: x ** 3)(4))

# Decorator for simple_function
def log_args(func):
	def wrapper(*args, **kwargs):
		print('Arguments:',args)
		print('Keyword arguments:', kwargs)
		return func(*args, **kwargs)
	return wrapper

# @log_args
def simple_function(x, y, a=2, b=4):
	return x + y + a + b

decorated_simple_function = log_args(simple_function)
print(decorated_simple_function(1, 2, a=3, b=4))
# print(simple_function(1, 2, a=3, b=4))

# Decorator for sub function with argument
def invoke_as(name=None):
	name = 'stranger' if not name else name
	def decorator(func):
		def wrapper(x, y):
			print('Hello, {}!'.format(name))
			result = func(x, y)
			print('Goodbye, {}!'.format(name))
			return result
		return wrapper
	return decorator

@invoke_as('Alex')
def sub(x, y):
	print('Function sub() is invoked!')
	return x - y

# decorator = invoke_as('Alex')
# decorated_sub = decorator(sub)
# decorated_sub(6, 2)
print(sub(6, 2))

