def remove_duplicates(string):
    uniqueCharacters = ""
    for i in string:
        if i not in uniqueCharacters:
            uniqueCharacters += i
    return uniqueCharacters

def is_pangram(string):
    string = remove_duplicates(string)
    string = "".join(sorted(string))
    print(string)
    if string.lower() == "abcdefghijklmnopqrstuvwxyz":
        return True
    return False



print(is_pangram("This isn't a pangram!"))
print(is_pangram("The quick brown fox jumps over the lazy dog"))

