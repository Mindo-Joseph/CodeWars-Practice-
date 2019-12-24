import math
def find_next_square(sq):
    num = math.sqrt(sq)
    if num % 1 != 0:
        return -1
    else:
        return int((num+1)**2)



    
        