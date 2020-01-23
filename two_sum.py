def two_sum(numbers,target):
    lookup = {}
    for i, num in enumerate(numbers):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

print(two_sum([1234,5678,9012], 14690))

