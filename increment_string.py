def increment_string(string):
    leading_digits = ""
    original_string = string
    if string == "" or not string[-1].isdecimal():
        return string + "1"
    for i, number in enumerate(string[::-1]):
        if number.isdecimal() and number != "0":
            leading_digits += number
            string = string[-i:]
    return string[:-1] + leading_digits

print(increment_string("bar001"))
print(increment_string("bar009"))
print(increment_string(""))

