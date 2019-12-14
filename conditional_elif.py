# Запустить это - python conditional_elif.py

# Оценка от 0 до 100 за тест
mark = int(input('Please enter your mark: '))

# Условный переход
if mark < 0:  # условие №1
    print("Something is wrong. Must be higher than 0!")  # если условие №1 истинно
elif mark < 25:  # условие №2
    print("It's a bad attempt. Try again!")  # если условие №2 истинно
elif mark >= 25 and mark < 50:  # условие №3
    print("You can be better. Once again!")  # если условие №3 истинно
elif mark >= 50 and mark < 75:  # условие №4
    print("Good enough. Maybe once again?")  # если условие №4 истинно
elif mark >= 75 and mark <= 100:  # условие №5
    print("Good job! You are the best!")  # если условие №5 истинно
else:
    print("Something is wrong. Must be lower than 100!")  # если никуда раньше не зашли



is_wrong = mark < 0 or mark > 100
is_bad = mark < 25
can_be_better = mark >= 25 and mark < 50
is_good_enough = mark >= 50 and mark < 75
is_good_job = mark >= 75 and mark <= 100

if is_wrong:
	print("Something is wrong. Must be higher than 0!")
elif is_bad:
	print("It's a bad attempt. Try again!")
elif can_be_better:
	print("You can be better. Once again!")
elif is_good_enough:
	print("Good enough. Maybe once again?")
elif is_good_job:
	print("Good job! You are the best!")
