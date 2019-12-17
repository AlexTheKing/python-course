'''
Построить лесенку вида:
[
["#", "_", "_"],
["#", "#", "_"],
["#", "#", "#"]
]
'''

from pprint import pprint

n = 4

pprint([['#']*i + ['_']*(n-i) for i in range(1, n)])
