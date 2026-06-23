def calculate_prefix_sum_in_place(arr):
    # arr is a list of integers
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]
        
def sumOddLengthSubarrays(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    
    # Build prefix sum
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    