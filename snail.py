
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
""" def snail(array):
    result = []
    for i in array[0]:
        result.append(i)
    result.append(array[1][-1])
    for i in reversed(array[2]):
        result.append(i)
    result.append(array[1][0])
    result.append(array[1][1])
    return result """

def snail(array):
    result = []
    for i, subArray in enumerate(array):
        if i == 0:
            for x in subArray:
                result.append(x)
        if i == len(array) - 1:
            for x in subArray[::-1]:
                result.append(x)
        



    


print(snail([[1,2,3], [8,9,4], [7,6,5]]))
if snail(array) == expected:
    print(True)
