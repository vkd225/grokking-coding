def generateDocument(characters, document):
    chars = {}

    for c in characters:
        if c not in chars:
            chars[c] = 0

        chars[c] += 1

    for d in document:
        if d in chars:
            chars[d] -= 1
            if chars[d] == 0:
                chars.pop(d)
        else:
            return False


    return True