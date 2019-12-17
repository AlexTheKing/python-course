# Запустить это - python files.py

# Файлы это потоки данных, они должны быть открыты и закрыты по окончанию работы с ними
filename = 'test.txt'

file = open(filename, 'w')  # w - режим write (запись), еще есть r - режим read (чтение)
words = ["Hello\n", "World\n", "In\n", "Files\n"]  # \n - символ переноса строки
for word in words:
	file.write(word)
file.close()  # закрываем файл

# Чтобы не забывать его закрыть, можно воспользоваться конструкцией with..as
# Она сама закроет файл как только выполнится весь код внутри
with open(filename, 'r') as file:
	for line in file:
		print(line)
