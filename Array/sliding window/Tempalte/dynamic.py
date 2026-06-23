# initialize left = 0
# initialize window_state (sum, count, frequency map, etc.)
# initialize min_or_max_result

for right in range(len(arr)):
    # update window_state to include arr[right]  # expand the window

    while window_state violates the condition:
        # 
        # update window_state to exclude arr[left]  # shrink the window
        left += 1  # move left pointer forward
        # update min_or_max_result (if needed)

return min_or_max_result


# example
def length_of_longest_substring(s: str) -> int:
    # initialize left = 0
    left = 0

    # initialize window_state (frequency set for characters)
    window_state = set()

    # initialize min_or_max_result
    max_length = 0

    for right in range(len(s)):
        # update window_state to include s[right]  # expand the window
        while s[right] in window_state:
            # update window_state to exclude s[left]  # shrink the window
            window_state.remove(s[left])
            left += 1  # move left pointer forward

        window_state.add(s[right])

        # update max result after window is valid
        max_length = max(max_length, right - left + 1)

    return max_length