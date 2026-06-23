def maximumSizeSubarray(arr,k):

    ans=0
    currSum=0
    seen={0:-1}

    for i,num in enumerate(arr):

        currSum+=num
        diff= currSum-k

        if diff in seen:
            ans= max(ans, i-seen[diff] )
        
        if currSum not in seen:  # we are not storing every time because we want eariest index for maximum length
            seen[currSum]=i

    return ans             