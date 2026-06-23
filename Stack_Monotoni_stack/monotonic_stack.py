def monotonic_stack_template(nums):
    n = len(nums)
    result = [0] * n
    stack = []  # Use list as stack in Python

    for i in range(n):
        # While stack is not empty and current element violates monotonic property
        while stack and violates_monotonic_property(nums[stack[-1]], nums[i]):
            index = stack.pop()
            result[index] = i  # Example: store index difference or custom value

        # Push the current index onto the stack
        stack.append(i)

    return result

# Helper function to define the monotonic property
def violates_monotonic_property(prev, curr):
    # Example: for strictly decreasing stack (Next Greater Element)
    return curr > prev

# Example usage:
nums = [2, 1, 2, 4, 3]
res = monotonic_stack_template(nums)
print(res)


# store indices than element 