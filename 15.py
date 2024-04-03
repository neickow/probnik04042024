for A in range(1, 100):
    i=0
    for x in range(1, 100):
        f = (x//50 > 3) or (not (x//13 > 3)) or (x//A > 6)
        if f:
            i+=1
    if i==99:
        print(A)
        break