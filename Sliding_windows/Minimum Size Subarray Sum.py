

def minimumSubArray(arr,target):

    left=0
    min_lenght=float('inf')
    sum=0

    for right in range(len(arr)):

        sum+=arr[right]

        while sum>=target:
            min_lenght=min(min_lenght,right-left+1)
            sum-=arr[left]
            left+=1

    return 0 if min_lenght==float('inf')  else min_lenght        
            


