def remove_duplicates(string):
    uniqueCharacters = ""
    for i in string:
        if i not in uniqueCharacters:
            uniqueCharacters += i
    return uniqueCharacters

def remove_nonalpha(string):
    return ''.join([i for i in string if i.isalpha()])