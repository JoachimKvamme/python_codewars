
def valid_braces(string):
    if not check_if_correct_number_of_braces(string):
        return False
    if not check_distance_between_braces(string):
        return False
    return True

def check_if_correct_number_of_braces(string):
    if string.count("{") != string.count("}"):
        return False
    if string.count("(") != string.count(")"):
        return False
    if string.count("[") != string.count("]"):
        return False
    return True

def check_distance_between_braces(string):
    for i, brace in enumerate(string):
        if brace == "{":
            if string[i:].find("}") == -1:
                return False
            distance = string.find("}", i) - i
            print(distance)
            if distance % 2 == 0:
                return False
        if brace == "[":
            if string.find("]", i) == -1:
                return False
            distance = string.find("]", i) - i
            print(distance)
            if distance % 2 == 0:
                return False
        if brace == "(":
            if string.find(")", i) == -1:
                return False
            distance = string.find(")", i) - i
            print(distance)
            if distance % 2 == 0:
                return False
    return True

def check_order_of_braces(string):
    openingOrder = []
    closingOrder = []
    for brace in string:
        if brace == "{":
            openingOrder.append(1)
        if brace == "[":
            openingOrder.append(2)
        if brace == "(":
            openingOrder.append(3)
        if brace == "}":
            closingOrder.append(1)
        if brace == "]":
            closingOrder.append(2)
        if brace == ")":
            closingOrder.append(3)
    if openingOrder[::-1] == closingOrder:
        return True
    print(openingOrder, closingOrder)

check_order_of_braces("(({{[[]]}}))")

print(valid_braces("()"))
print(valid_braces("{[}]"))
print(valid_braces("[(])"))
print(valid_braces("([{}])"))
print(valid_braces("{}()[]"))


print(valid_braces("(({{[[]]}}))"))
print(valid_braces("([}{])"))