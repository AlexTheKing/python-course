'''
The Karaca's Encryption Algorithm
Написать алгоритм кодирования сообщений, согласно шагам:
На входе: apple
1) Инвертировать строку: "elppa"
2) Заменить гласные: 8lpp4
a => 4
e => 8
o => 7
u => 9
3) Добавить "aca" к концу сообщения: 8lpp4aca
'''

vowels = {
	'a': 4,
	'e': 8,
	'o': 7,
	'u': 9
}

apple = 'apple'
message = ''.join([
	letter if letter not in vowels.keys() else str(vowels[letter])
	for letter in apple[::-1]
]) + 'aca'



print(message)












