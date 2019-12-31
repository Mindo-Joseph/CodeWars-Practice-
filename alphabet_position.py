from string import ascii_lowercase

letters = {letter:str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

def alphabet_position(text):
    text = text.lower()
    numbers = [letters[character] for character in text if character in letters]
    return ' '.join(numbers)