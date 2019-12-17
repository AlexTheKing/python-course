import timeit

print("List concatenation:", timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print("Element search:", timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))

def f(x):
	return x**2

def g(x):
	return x**4

def h(x):
	return x**8

print("Function invokation:", timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))