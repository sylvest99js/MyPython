

for pred in (1,0):
    print("pred = ",pred)
    B = [ [2, 3, 2], [4, 3, 6], [0, 0, 4] ]
    print("B",B)
    if pred:
        print("Using loop: for ii in range( len( B ) )")
            
        # this makes a genuine deep copy
        C = []
        for ii in range( len( B ) ):
            C.append(B[ii].copy())
    else:
        print("Using C = B[:][:].copy()")
        # this makes a somewhat deep copy ????
        C = B[:][:].copy()


    print("pop row 0  of B")
    B.pop(0)
    print("B",B)
    print("C",C)

    print("double B")
    B *= 2
    print("B",B)
    print("C",C)

    print("double a row 1 of B")
    B[1] *= 2
    print("B",B)
    print("C",C)
