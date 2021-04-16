def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    without_row_1 = matrix[1: len(matrix)]

    det = 0
    factor = -1 # first term in sum should have  + sign
    for mmm in range(len(matrix)):
        minor = []
        # Now build the minor by deleting the mmm column
        # We build row by row because we don't know a
        # way to make a deep copy of a list of lists
        for nn in range(len(without_row_1)):
            aa = without_row_1[nn].copy()
            aa.pop(mmm)
            minor.append(aa)
            
        dm = determinant(minor)
        factor *= -1  # alternate signs in sum
        det += factor * matrix[0][mmm] * dm
        # Just for testing
        # print("minor", minor)
        # print("determinant(minor)", dm)

    return det


B = [ [2, 3, 2], [4, 3, 6], [0, 0, 4] ]


print("determinant(B) = ", determinant(B))
