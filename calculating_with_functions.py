

def zero(operator=0):
    if type(operator) is not list:
        return 0
    return makeOperations(operator[0], 0, operator[1])
def one(operator=1): 
    if type(operator) is not list:
        return 1
    return makeOperations(operator[0], 1, operator[1])
def two(operator=2):
    if type(operator) is not list:
        return 2
    return makeOperations(operator[0], 2, operator[1])
def three(operator = 3):
    if type(operator) is not list:
        return 3
    return makeOperations(operator[0], 3, operator[1])
    pass #your code here
def four(operator=4):
    if type(operator) is not list:
        return 4
    return makeOperations(operator[0], 4, operator[1])
def five(operator=5):
    if type(operator) is not list:
        return 5
    return makeOperations(operator[0], 5, operator[1])
def six(operator=6):
    if type(operator) is not list:
        return 6
    return makeOperations(operator[0], 6, operator[1])
def seven(operator=7):
    if type(operator) is not list:
        return 7
    return makeOperations(operator[0], 7, operator[1])
def eight(operator=8):
    if type(operator) is not list:
        return 8
    return makeOperations(operator[0], 8, operator[1])
def nine(operator=9):
    if type(operator) is not list:
        return 9
    return makeOperations(operator[0], 9, operator[1])

def plus(number):
    return ["+", number]
    pass #your code here
def minus(number): 
    return ["-", number]
    pass #your code here
def times(number):
    return ["*", number]
    pass #your code here
def divided_by(number):
    return ["/", number]
    pass #your code here

def makeOperations(operator, x, y):
    match operator:
        case "+":
            return x + y
    match operator:
        case "-":
            return x - y
    match operator:
        case "*":
            return x * y
    match operator:
        case "/":
            return x // y

print(two(times(five())))