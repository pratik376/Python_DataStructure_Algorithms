# initialize window_sum = 0
# initialize max_result (or other required value)

# Set up the initial window
for i in range(k):
    window_sum += arr[i]

max_result = window_sum  # initialize result

# Slide the window across the array
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]  # add new element, remove old element
    # update max_result (or other computation)

return max_result



# example

def find_max_average(nums, k):
    n = len(nums)

    # Edge case check
    if k > n or k == 0:
        return 0.0

    # Compute the sum of the first k elements
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]

    # Initialize max_sum as the first window sum
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, n):
        window_sum -= nums[i - k]  # remove element leaving the window
        window_sum += nums[i]      # add new element entering the window
        max_sum = max(max_sum, window_sum)

    # Return maximum average
    return max_sum / k
