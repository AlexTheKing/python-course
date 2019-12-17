import random

print("Random choice of apple, banana, pear:", random.choice(['apple', 'banana', 'pear']))
print("Sampling 10 random ints from 0..100:", random.sample(range(100), 10))
print("Random from 0..1:", random.random())
print("Random integer from 0..7:", random.randrange(6))

a = list(range(10))
print("List a:", a)
random.shuffle(a)
print("Shuffled list:", a)