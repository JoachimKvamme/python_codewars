def increment_string(string):
    leading_digits = ""
    zeroes = ""
    reversed_string = string[::-1]
    if string == "" or not string[-1].isdecimal():
        return string + "1"
    if string[-1] == "0":
         return string[:-1] + "1"
    for i, number in enumerate(reversed_string):
        print(i)
        print(len(string))
        if number.isdecimal():
            leading_digits += number
            if number == "0":
                zeroes += "0"
                if reversed_string[i+1] == "0":
                    string = string[:-i]
                    break
        if not number.isdecimal():
                string = string[:-i]
                break


    print(string)
    leading_digits = leading_digits[::-1]
    increment = int(leading_digits) + 1
    print(increment)
    if zeroes != "" and leading_digits[-1] == "9":
         return string[:-1] + str(increment)
    
    print(leading_digits)
    incremented_string = string + str(increment)
    print(incremented_string)
    return incremented_string


print(increment_string("bar1"))
print(increment_string("bar001"))
print(increment_string("bar100"))
print(increment_string("bar009"))
print(increment_string(""))
print(increment_string("O-_5660\\luu?+q80650800009"))
print(increment_string("foobar001"))
print(increment_string("foobar00"))
print(increment_string("fo99obar99"))

# 'O-_5660\\luu?+q80650800009': 'O-_5660\\luu?+q806508000010' should equal 'O-_5660\\luu?+q80650800010'