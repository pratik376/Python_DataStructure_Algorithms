def two_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left + 1, right + 1]  # ✅ directly return indices

numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))
