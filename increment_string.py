def increment_string(string):
    leading_digits = ""
    zeroes = ""
    if string == "" or not string[-1].isdecimal():
        return string + "1"
    for i, number in enumerate(string[::-1]):
        if number.isdecimal() and number != "0":
            leading_digits += number
        if number.isdecimal() and number == "0":
            zeroes += "0"
        if i == len(string):
            string = string[-i]
    print(string)
    
    return string[:-1] + leading_digits

print(increment_string("bar001"))
print(increment_string("bar009"))
print(increment_string(""))
print(increment_string("O-_5660\\luu?+q80650800009"))

# 'O-_5660\\luu?+q80650800009': 'O-_5660\\luu?+q806508000010' should equal 'O-_5660\\luu?+q80650800010'