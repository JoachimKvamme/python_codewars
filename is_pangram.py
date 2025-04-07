def remove_duplicates(string):
    uniqueCharacters = ""
    for i in string:
        if i not in uniqueCharacters:
            uniqueCharacters += i
    return uniqueCharacters

def remove_nonalpha(string):
    return ''.join([i for i in string if i.isalpha()])

def is_pangram(string):
    string = string.lower()
    string = remove_duplicates(string)
    string = "".join(sorted(string))
    string = remove_nonalpha(string)
    if string.strip() == "abcdefghijklmnopqrstuvwxyz":
        return True
    return False




print(is_pangram("This isn't a pangram!"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))

