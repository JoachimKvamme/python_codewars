def max_sequence(array):
    sum = 0
    intermediarySum = 0
    for number in array:
        intermediarySum += number
        if intermediarySum < 0:
            intermediarySum = 0
        if intermediarySum > sum:
            sum = intermediarySum
    return sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    
