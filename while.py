# Запустить это - python while.py

# Посчитать от 1 до 10
print("Count 1..10")

counter = 1
while counter <= 10:
    print(counter)
    counter += 1  # counter = counter + 1

# Посчитать от 1 до 10 с использованием break
print("Count 1..10 using break")

counter = 1
while True:
    if counter > 10:
        break
    print(counter)
    counter += 1

# Посчитать от 1 до 10, пропуская нечетные числа
print("Count 1..10 skipping odd numbers")

counter = 0
while counter <= 10:
    counter += 1
    if counter % 2 == 1:
        continue
    print(counter)
