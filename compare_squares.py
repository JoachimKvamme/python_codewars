def comp(array1, array2):
    if array1 == [] and array2 == []:
        return True
    if array1 == [] or array2 == [] or len(array1) != len(array2):
        return False
    array_squared = []
    for i in array1:
        array_squared.append(i*i)
    array_squared = sorted(array_squared)
    array2 = sorted(array2)
    if array_squared == array2:
        return True
    return False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1,a2))