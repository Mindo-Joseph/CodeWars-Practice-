def comp(arr1,arr2):
    squared = list(map(lambda x: x**2, arr1)) 
    squared.sort()
    arr2.sort()
    for i in range(0,len(squared)-1):
        if squared[i] != arr2[i]:
            return False
    return True
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))