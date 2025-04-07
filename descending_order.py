def descending_order(number):
    stringInt = str(number)
    stringInt = "".join(sorted(stringInt))[::-1].strip()
    return int(stringInt)

print(descending_order(15))


