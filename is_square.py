import math
def is_square(num):
    if num < 0:
        return False
    return math.sqrt(num).is_integer()

