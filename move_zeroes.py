

def move_zeros(zeroList):
    nonZeroList = [x for x in zeroList if x != 0]
    for x in range(0, zeroList.count(0)):
        nonZeroList.append(0)
    return nonZeroList

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]