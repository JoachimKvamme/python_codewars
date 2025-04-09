
def valid_braces(string):
    openingBraces = []
    check_number_of_braces(string)
    for brace in string:
        if brace == "{" or brace == "[" or brace == "(":
            openingBraces.append(brace)
        if brace == "}":
            if len(openingBraces) == 0:
                return False
            if openingBraces[-1] != "{":
                return False
            openingBraces.pop()
        if brace == "]":
            if len(openingBraces) == 0:
                return False
            if openingBraces[-1] != "[":
                return False
            openingBraces.pop()
        if brace == ")":
            if len(openingBraces) == 0:
                return False
            if openingBraces[-1] != "(":
                return False
            openingBraces.pop()
    if len(openingBraces) != 0:
        return False
    return True

def check_number_of_braces(string):
    openingBraces = []
    closingBraces = []
    for brace in string:
        if brace == "{" or "[" or "(":
            openingBraces.append(brace)
        if brace == "}" or "]" or ")":
            closingBraces.append(brace)
    if len(closingBraces) != len(openingBraces):
        return False
    return True

print(valid_braces("())({}}{()][]["))
print(valid_braces("{[}]"))
print(valid_braces("[(])"))
print(valid_braces("([{}])"))
print(valid_braces("{}()[]"))


print(valid_braces("(({{[[]]}}))"))
print(valid_braces("([}{])"))