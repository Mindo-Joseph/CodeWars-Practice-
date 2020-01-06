
new_n = str(1244)
arr = []
for i in new_n:
    arr.append(i)

if arr[len(arr)-1] > arr[len(arr)-2]:
    arr[len(arr)-1],arr[len(arr)-2] = arr[len(arr)-2],arr[len(arr)-1]
else:
    if arr[len(arr)-1] == arr[len(arr)-2]:
        arr[len(arr)-2],arr[len(arr)-3] = arr[len(arr)-3],arr[len(arr)-2]

print(''.join(arr))