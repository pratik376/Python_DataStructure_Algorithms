def calculate_prefix_sum_in_place(arr):
    
    
    arr[0]=arr[0]
    max_sum=max(0,arr[0])
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]

        max_sum=max(max_sum,arr[i])

    return max_sum    