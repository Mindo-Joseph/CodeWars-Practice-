def find_it(arr):
    counts = {}
    for element in arr:
        if element not in counts:
            counts[element]= 1
        else:
           counts[element] += 1
    for key, value in counts.items():
        if value%2 != 0:
            return int(key)

    return None

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))