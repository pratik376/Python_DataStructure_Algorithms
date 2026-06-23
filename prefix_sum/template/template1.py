def calculate_prefix_sum_in_place(arr):
    # arr is a list of integers
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]
