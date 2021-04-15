def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    tempmatrix = matrix[1: len(matrix)]

    det = 0
    factor = -1
    for mmm in range(len(matrix)):
        minor = []
        factor *= -1  # alternate sighs
        for nn in range(len(tempmatrix)):
            aa = tempmatrix[nn].copy()
            aa.pop(mmm)
            minor.append(aa)
        dm = determinant(minor)
        det += factor * matrix[0][mmm] * dm
        # print("minor", minor)
        # print("determinant(minor)", dm)

    return det


B = [[1, 3, 2], [0, 3, 6], [0, 0, 1]]

C = B

print("determinant(B) = ", determinant(B))
