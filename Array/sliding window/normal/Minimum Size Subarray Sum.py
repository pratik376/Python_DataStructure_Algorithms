def minimun_size_sub_array(arr,target):

    window_sum=0
    res=float('inf')
    left=0

    for right in range(len(arr)):
        window_sum+= arr[right]

        while window_sum>=target and left<=right:

            res= min(right-left+1, res)
            window_sum-=arr[left]
            left+=1

    return res if res!= float('inf') else 0
        