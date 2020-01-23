
def increment_string(strng):
    numbers = []
    new_strng = []
    strng_list = list(strng)
    for char in strng_list:
        if str(char).isdigit():          
            numbers.append(char)
        else:
            new_strng.append(char)
    new_strng = "".join(new_strng) 

    if not numbers:
        return new_strng + str(1)
    else:
        return new_strng + str(int("".join(numbers))+1)

            
        
    
        
print(increment_string("foo23"))