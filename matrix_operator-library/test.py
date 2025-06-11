from lib import add_matrices, subtract_matrices, multiply_matrices

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [1, 2, 3]]
C = [[1, 2], [3, 4], [5, 6]]

print("A + B =", add_matrices(A, B))
print("A - B =", subtract_matrices(A, B))
print("A * C =", multiply_matrices(A, C))
