import pandas as pd

data = {
	'Apples': [3, 2, 0, 1],
	'Oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases)

print(purchases.loc['June'])

print(purchases.columns)

print(purchases[purchases['Apples'] > 2])