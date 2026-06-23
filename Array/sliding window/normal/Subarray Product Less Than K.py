def subarrayProductLessThanK(arr,k):

    if k<=1:
        return 0
    
    ans=0
    left=0
    current_product=1

    for right in range(len(arr)):

        current_product*=arr[right]

        while current_product >= k:
            current_product //= arr[left]
            left+=1

        ans+= right-left+1    

        # Every time we expand a string, we gain additional subarray amount that equal to the new string length (r-l+1)


# We cannot use the "Exactly(K) = AtMost(K) - AtMost(K-1)" trick here because this problem deals with a continuous constraint (product < K), not a discrete "exactly K" count. The AtMost trick works only for discrete counts, like "number of distinct integers".
    