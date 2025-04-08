def sort_array(source_array):
    evenNumbersWithIndex = makeEvenNumberDictionary(source_array)
    oddSortedNumbers = sorted(removeEvenNumbers(source_array))
    print(oddSortedNumbers)
    for index, value in evenNumbersWithIndex.items():
        oddSortedNumbers.insert(index, value)
    
    return oddSortedNumbers

def makeEvenNumberDictionary(array):
    evenNumberedDictionaryWithIndexKeys = {}
    for i, number in enumerate(array):
        if number % 2 == 0:
            evenNumberedDictionaryWithIndexKeys.update({i : number})
    return evenNumberedDictionaryWithIndexKeys

def removeEvenNumbers(array):
    loopingArray = array.copy()
    for number in loopingArray:
        if number % 2 == 0:
            array.remove(number)
    return array



print(makeEvenNumberDictionary([5, 3, 2, 8, 1, 4]))
print(removeEvenNumbers([5, 3, 2, 8, 1, 4]))


print(sort_array([5, 3, 2, 8, 1, 4]))