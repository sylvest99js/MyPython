def determinant(A):
    if len(A) == 1:
        return A[0][0]

    tempA = A[1 : len(A)]

    det = 0
    factor = -1
    for mmm in range(len(A)):
        minor = []
        factor *= -1  # alternate sighs
        for nn in range(len(tempA)):
            aa = tempA[nn].copy()
            aa.pop(mmm)
            minor.append(aa)

        det += factor * A[1][mmm] * determinant(minor)
        print("detsofar", det)

    return det


B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

C = B

print(determinant(B))
