# Запустить это - python conditional_if.py

right_name = "Alex"
right_password = "12345678"

name = input("Please enter the name: ")
password = input("Please enter the password: ")

access_granted = "ACCESS GRANTED! You are in!"
access_denied = "ACCESS DENIED! Wrong name or password!"

# Условный переход
if name == right_name and password == right_password:  # условие
 print(access_granted)  # если условие истинно
 print('123')
 print(123)
else:
   print(access_denied)  # если условие ложно


'''
Это
    многострочный
        комментарий
is_alex = name == right_name
is_password_right = password == right_password
can_login = is_alex and is_password_right
if can_login:
    print(access_granted)
else:
    print(access_denied)

print(access_granted if can_login else access_denied)
'''