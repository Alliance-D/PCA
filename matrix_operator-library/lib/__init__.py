def validate_same_size(A, B):
    return len(A) == len(B) and all(len(row_a) == len(row_b) for row_a, row_b in zip(A, B))

def add_matrices(A, B):
    if not validate_same_size(A, B):
        raise ValueError("Helooo, remember matrices must have the same dimensions to add.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    if not validate_same_size(A, B):
        raise ValueError("Please remember matrices must have the same dimensions to subtract.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Check well, Number of columns in A must equal number of rows in B to multiply.")
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_product = 0
            for k in range(len(B)):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result
