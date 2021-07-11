import numpy as np

# compare lists to ndarrays

print("Python list operations:")
a = [1, 2, 3]
b = [4, 5, 6]
print("a+b:", a + b)
try:
    print(a * b)
except TypeError:
    print("a*b has no meaning for Python lists")
print()
print("numpy array operations:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a+b:", a + b)
print("a*b:", a * b)

c = np.array([[1, 2], [3, 4]])
print("c:")
print(c)
print("c.sum(axis=0):", c.sum(axis=0))
print("c.sum(axis=1):", c.sum(axis=1))
