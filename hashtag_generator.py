def generate_hashtag(string):
    if string == "":
        return False
    hashtag = "#"
    word = ""
    for i in string:
        if i.isalpha:
            word += i.lower()
        if i == " " and word != "":
            word = word.strip()
            hashtag += word.capitalize()
            word = ""
    if word != "":
        hashtag += word.capitalize()
    if len(hashtag.strip()) > 140:
        return False
    return hashtag.strip()


print(generate_hashtag('Codewars'))
print(generate_hashtag('      Codewars'))