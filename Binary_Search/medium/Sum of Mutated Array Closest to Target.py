def target(arr, target):


    l, r= min(arr), max(arr)
    best_x=0
    min_diff= float('inf')
    

    while l<=r:

        mid = (l+r)//2
        
        curr_sum=0
        for val in arr:

            if val> mid:
                curr_sum+= mid
            else:
                curr_sum+= val

        diff= abs(curr_sum- target)

        if diff < min_diff or (diff== min_diff and mid < best_x):
            min_diff=diff
            best_x=mid       

        if curr_sum> target:
            r=mid-1
        else:
            l= mid+1    
    return best_x                  
