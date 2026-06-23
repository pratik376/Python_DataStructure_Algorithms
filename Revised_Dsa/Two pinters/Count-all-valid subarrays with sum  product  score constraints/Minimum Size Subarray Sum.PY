def minimumSizeSubarray(arr, target):

    left=0

    answer= float('inf')

    window_sum=0


    for right in range(len(arr)):

        window_sum+=arr[right]


        while window_sum >=target:

            answer=min(answer, right-left+1)

            answer-= arr[left]

            left+=1

    return 0 if answer== float('inf') else answer    






