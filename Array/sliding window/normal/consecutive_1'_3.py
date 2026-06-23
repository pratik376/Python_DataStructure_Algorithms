
def concecutives1(arr,k):

    zero_count=0

    left=0

    max_count=float('-inf')

    for right in range(len(arr)):

        if arr[right]==0:
            zero_count +=1

        

        while zero_count > k:
            if arr[left]==0:
                zero_count-=1

            left+=1

        max_count=max(max_count,right-left+1)    

    return max_count    


