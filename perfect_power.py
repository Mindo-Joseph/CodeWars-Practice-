from math import sqrt
def isPP(n):
    if sqrt(n)%1 == 0:
        return [int(sqrt(n)),2]
    else:
        return 


print(isPP(5))