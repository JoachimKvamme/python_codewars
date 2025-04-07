def accum(st):
    accumString = ""
    string = st.replace("-", "")
    string = string.lower()
    for count, letter in enumerate(string):
        for i in range(0, count+1):
            if i == 0 and letter.isalpha():
                Cletter = letter.upper()
                accumString += Cletter
                string = string.replace(Cletter, "")
            if i != 0 and letter.isalpha():
                accumString += letter
                string = string.replace(letter, "")
            if i == count:
                accumString += "-"
    return accumString[:-1]

print(accum("ZpglnRxqenU"))

print(accum("a-b"))

#'Z-Pp-Ggg-Llll-Nnnnn-RRRRRR-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-UUUUUUUUUUU-' should equal 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu'