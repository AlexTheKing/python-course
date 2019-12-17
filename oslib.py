import os

# Возвращает рабочую директорию
print(os.getcwd())

# Это выполняется в командной оболочке
os.system('echo Hello Shell!')

# Создание каталога
os.mkdir('mydir')

for root, directories, files in os.walk('.'):
	print('Root:', root)
	print('Directories:', directories)
	print('Files:', files)
	print('===================================')

