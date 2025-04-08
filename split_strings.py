def solution(text):
    substrings = []
    for i in range(0, len(text)):
        if len(text) != 0:
            if len(text[:2]) < 2:
                substrings.append(text[:2] + "_")
                break
            substrings.append(text[:2])
            text = text[2:]
    return substrings


print(solution("asdfads"))