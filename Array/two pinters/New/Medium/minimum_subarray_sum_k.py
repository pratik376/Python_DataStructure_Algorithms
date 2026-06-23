def minimum_sum(arr, target):

    sum=0
    left=0
    min_length=float("inf")

    for right in range(len(arr)):

        sum+=right

        while sum>= target:

            min_length=min(min_length, right-left+1)
            sum-=arr[left]
            left+=1

    return 0 if min_length== float('inf') else min_length        

