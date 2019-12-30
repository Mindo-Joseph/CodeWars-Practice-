def getCount(inputStr):
    num_vowels = 0
    vowels = "aeiou"
    for char in inputStr:
        if char in vowels:
            num_vowels+=1
    
    return num_vowels

