def first_non_repeating_letter(string):
    looping_string = string.lower()
    if string == "":
        return ''
    for i, letter in enumerate(looping_string):
        if looping_string.count(letter) == 1:
            return string[i]
    return ""