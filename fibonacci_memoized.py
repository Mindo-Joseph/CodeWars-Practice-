nums = {}
def fibonacci(n):
    if n <=2:
        return 1
    if n in nums:
        return nums[n]
    else:
        num = fibonacci(n-1) + fibonacci(n-2)
        nums[n] = num
        return num