def minimumOperationsToReduceX(arr,x):

    


    left=0
    length=-1

    target= sum(arr)-x
    window_sum=0

    if target < 0:
     return -1

    if target == 0:
     return len(arr)


    for right in range(len(arr)):

        window_sum+=arr[right]


        while left<=right and  window_sum >target:

            window_sum-=arr[left]
            left+=1

        if window_sum == target:    

         length= max(length, right-left+1) 

    answer= len(arr)- length

    return answer if length != -1 else -1

             


