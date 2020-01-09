import re
def pig_it(text):
    new_text = re.findall(r"[\w']+|[.,!?;]",text)
    new_text2 = []

    for word in new_text:
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(word) == None:
            word = word[1:] + word[0] + "ay"
        new_text2.append(word)

    return " ".join(new_text2)
