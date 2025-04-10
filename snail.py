
array = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10 ,9 ,8 ,7]]
expected = [1,2,3,4,5,6,7,8,9]

def snail(array):
    if array == None or array == [[]]:
        return []
    result = []
    top = 0
    bottom = len(array) - 1
    right = int(-1)
    left = int(0)
    for x in range(0, bottom + 1):
        #left => right top
        for i in range(top, bottom+1):
            result.append(array[top][i])
        top += 1
        # top => bottom right
        for i in range(top, bottom + 1):
            result.append(array[i][right])
        # right => left bottom
        for i in range(top, bottom + 1):
            reversedbottom = array[bottom][::-1]
            result.append(reversedbottom[i])
        bottom += -1
        # bottom => top left
        for i in range(top, bottom +1):
            result.append(array[i][left])
        left += 1
        right -= 1
    return result
top = 0
i = 0

print(array[top][i])
print(snail(array))
        