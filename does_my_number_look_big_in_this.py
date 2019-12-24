def narcissistic ( value ):
    total = 0
    value = str(value)
    length = len(value)
    for i in value:
        total += pow(int(i),length)
    return total == int(value)
   


        

    