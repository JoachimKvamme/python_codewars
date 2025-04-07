def to_camel_case(text):
    for idx, i in enumerate(text):
        if text[idx] == "-" or text[idx] == "_":
            modified_text = text.replace(text[idx:idx+2], text[idx+1:idx+2].upper(), 2) + "  "
            text = modified_text
         
    return text.strip()
print(to_camel_case("the-stealth-warrior"))



