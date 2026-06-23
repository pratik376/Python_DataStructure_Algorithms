def ReduceXToZero(arr,X):

    total_sum= sum(arr)
    target= total_sum- X

    currSum=0
    ans=-1
    seen={0:-1}

    if target< 0:
         return -1
    if target==0:
        return len(arr)


    for i, num in enumerate(arr):

        currSum+= num
        diff= currSum-target

        if diff in seen:
            ans= max(ans, i-seen[diff])
        
        if currSum not in seen: # here we want longer subarray so that less element removed
         seen[currSum]=i 

    return len(arr)- ans if ans!=-1 else -1       

# using sliding window
def minOperations(nums, x):
    total = sum(nums)
    target = total - x

    if target < 0:
        return -1  # impossible
    if target == 0:
        return len(nums)  # remove all

    max_len = -1
    curr_sum = 0
    left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        # shrink window from left if sum exceeds target
        while curr_sum > target and left <= right:
            curr_sum -= nums[left]
            left += 1

        # if window sum equals target, update max_len
        if curr_sum == target:
            max_len = max(max_len, right - left + 1)

    return len(nums) - max_len if max_len != -1 else -1