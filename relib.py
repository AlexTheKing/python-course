import re

print(re.findall(r'\bw[a-z]*', 'apple world banana wide orange web'))

regex = r'^[A-Z]{3}-[0-9]{3}$'
print(re.search(regex, 'AAA-001'))
print(re.search(regex, 'AA1-001'))
print(re.search(regex, 'ABA-021'))
print(re.search(regex, 'AZA-0Z1'))