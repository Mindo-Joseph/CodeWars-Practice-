def wave(strng):
    strng = str(strng)
    new = []
    for i, val in enumerate(strng[:]):
        upper = strng[i].upper()
        word = strng[:i] + upper + strng[i+1:]
        new.append(word)
    return new

print(wave(" gap "))