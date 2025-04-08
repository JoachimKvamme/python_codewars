def count(string):
    wordCount = {}
    uniqueCharacters = remove_duplicates(string)
    for i in string:
        if i in uniqueCharacters:
            numberOfInstances = string.count(i)
            wordCount.update({i: numberOfInstances})
            uniqueCharacters.replace(i, "")
    return wordCount

def remove_duplicates(string):
    uniqueCharacters = ""
    for i in string:
        if i not in uniqueCharacters:
            uniqueCharacters += i
    return uniqueCharacters


print(count('aabb'))