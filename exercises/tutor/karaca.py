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

word = input()

replacements = {
	'a': '4',
	'e': '8',
	'o': '7',
	'u': '9'
}

message = ''.join([
	replacements[letter] if letter in replacements.keys() else letter
	for letter in word[::-1]]
) + 'aca'