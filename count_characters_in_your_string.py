def count(string):
    wordCount = {}
    
    for i in string:
        numberOfInstances = i.count()
    return wordCount

def remove_duplicates(string):
    uniqueCharacters = ""
    for i in string:
        if i not in uniqueCharacters:
            uniqueCharacters += i
    return uniqueCharacters


count('aabb')