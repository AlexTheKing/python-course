# Запустить это - python exceptions.py

# Исключения - сообщают об исключительных ситуациях (когда что-то пошло не так)
# Язык позволяет их обрабатывать, например:
# Деление на ноль
x = 0
print("x:", x)
try:
	print("Result of 100 / x:", 100 / x)
except ZeroDivisionError:
	print("Zero division!")
finally:  # необязательный блок, выполнится и в случае исключения, и если его не будет
	print("Goodbye!")
# Без их обработки, в случае исключительной ситуации, программа прекращает свое выполнение
