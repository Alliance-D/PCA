# Matrix_operator
MatrixOps Library

A lightweight Python library for basic matrix operations, implemented from scratch using only core Python data structures. It provides functions to validate matrix dimensions and perform addition, subtraction, and multiplication of matrices.

Features

Dimension Validation: Ensure two matrices have the same dimensions before performing operations.

Matrix Addition & Subtraction: Element-wise operations on equal-sized matrices.

Matrix Multiplication: Standard row-by-column multiplication.

Pure Python: No external dependencies—uses only built-in lists and control structures.

## Usage

from matrixops import (
    validate_same_size,
    add_matrices,
    subtract_matrices,
    multiply_matrices
)

# Example matrices
a = [
    [1, 2, 3],
    [4, 5, 6]
]
b = [
    [7,  8,  9],
    [10, 11, 12]
]

# Validate dimensions
print(validate_same_size(a, b))  # True

# Addition
c = add_matrices(a, b)
print("a + b =", c)

# Subtraction
d = subtract_matrices(b, a)
print("b - a =", d)

# Multiplication (2×3 * 3×2 -> 2×2)
e = multiply_matrices(
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8], [9, 10], [11, 12]]
)
print("Product =", e)

# python
from matrixlib import add_matrices, subtract_matrices, multiply_matrices

API Reference

validate_same_size(A, B)

Checks that matrices A and B have the same number of rows and columns.

Parameters:

A, B (List[List[Number]]): Two matrices to compare.

Returns:

bool: True if dimensions match, False otherwise.

add_matrices(A, B)

Element-wise addition of two same-sized matrices.

Raises: ValueError if dimensions differ.

Returns: New matrix (List[List[Number]]) of sums.

subtract_matrices(A, B)

Element-wise subtraction (A - B) of two same-sized matrices.

Raises: ValueError if dimensions differ.

Returns: New matrix of differences.

multiply_matrices(A, B)

Standard matrix multiplication of A (m×n) by B (n×p), resulting in an (m×p) matrix.

Raises: ValueError if number of columns in A ≠ number of rows in B.

Returns: New matrix of products.

Error Handling

Addition/Subtraction: Raises ValueError with a clear message if matrix dimensions do not match.

Multiplication: Raises ValueError if inner dimensions are incompatible.


