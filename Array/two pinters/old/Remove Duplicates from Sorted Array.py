arr = [0,0,1,1,1,2,2,3,3,4]

current = arr[0]
i = 1

while i < len(arr):
    if arr[i] == current:
        del arr[i]
    else:
        current = arr[i]
        i += 1  # only move forward when element is unique

print(arr)

