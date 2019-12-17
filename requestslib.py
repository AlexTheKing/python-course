import requests


response = requests.get(
	'https://api.github.com',
	params={'q': 'requests+language:python'}
	)


print("Status code:", response.status_code)
print("Reponse:")
print(response.text)

deserialized = response.json()
print("Deserialized JSON:")
print(deserialized)

print("Headers:", response.headers)

