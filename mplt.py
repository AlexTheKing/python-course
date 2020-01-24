import matplotlib.pyplot as plt

X = []
Y = []

x = -5
while x < 5:
	y = x**2
	X.append(x)
	Y.append(y)
	x += 0.2


plt.plot(X, Y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()