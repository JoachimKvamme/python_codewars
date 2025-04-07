def get_middle(string):
    length = len(string)
    middle = int(length / 2)
    if length % 2 == 0:
        return string[middle-1:middle+1]
    if length % 2 != 0:
        return string[middle]


print(get_middle("test"))
print(get_middle("testing"))
