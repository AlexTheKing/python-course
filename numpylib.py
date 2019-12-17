import numpy as np

vector = np.array([1, 2, 3])
print('Vector:', vector)
print('Vector type:', type(vector))
print('Vector shape:', vector.shape)
print('Vector elements:', vector[0], vector[1], vector[2])
vector[0] = 5
print('Vector after changes:', vector)

print()

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print('Matrix:')
print(matrix)
print('Matrix shape:', matrix.shape)
print('Matrix indexation:', matrix[0, 0], matrix[0, 1], matrix[1, 0])

print('Zero-matrix:')
print(np.zeros((2, 2)))

print('Ones-matrix:')
print(np.ones((3, 2)))

print('Matrix filled with a constant:')
print(np.full((2,2), 7))

print('Identity matrix:')
print(np.eye(4))

print('Random matrix:')
print(np.random.random((3,3)))

print()

# Slicing and indexation
matrix = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print('Matrix:')
print(matrix)
print('Slicing last 2 rows and last 2 columns:')
m_slice = matrix[1:, 1:]
print(m_slice)
print('Changing slice:')
m_slice[1, 1] = 10
print(m_slice)
print('Matrix was changed also:')
print(matrix)

print()

matrix = np.array([[1, 2], [3, 4], [5, 6]])
print('Matrix:')
print(matrix)
print('Another way of indexation:')
print(matrix[[0, 1, 2], [0, 1, 0]])
print('The same as:')
print(np.array([matrix[0, 0], matrix[1, 1], matrix[2, 0]]))

print()

print('Range:')
print(np.arange(5))

print()

print('Boolean indexation (elements > 3):')
boolean_indexation = matrix > 3
print(boolean_indexation)
print(matrix[boolean_indexation])

print()

# Array math
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
print('Matrix X:')
print(X)
print('Matrix Y:')
print(Y)
print('X + Y:')
print(X + Y)
print('X - Y:')
print(X - Y)
print('X * Y:')
print(X * Y)
print('X / Y:')
print(X / Y)
print('sqrt(X):')
print(np.sqrt(X))
print('X x Y:')
print(np.dot(X, Y))

print()

# Sums
X = np.array([[1, 2], [3, 4]])
print('Matrix X:')
print(X)
print('Sum of elements:', np.sum(X))
print('Vertical sum:')
print(np.sum(X, axis=0))
print('Horizontal sum:')
print(np.sum(X, axis=1))

print()

# Transposed matrix
print('Transposed matrix X:')
print(X.T)