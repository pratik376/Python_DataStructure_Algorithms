def monotonic_stack_template(nums):
    n = len(nums)
    result = [0] * n

    stack = []  # Initialize empty stack (will store indices)

    for i in range(n):
        # While stack is not empty AND current element violates monotonic property
        while stack and violates_monotonic_property(nums[stack[-1]], nums[i]):
            index = stack.pop()      # Remove top element
            result[index] = i        # Example: store index difference (customizable)

        # Push current index
        stack.append(i)

    return result