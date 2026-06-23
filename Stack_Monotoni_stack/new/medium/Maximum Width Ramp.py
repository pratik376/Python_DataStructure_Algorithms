def maximumWidh(arr):

    max_right= [0] * len(arr)
    i=len(arr)-1
    prev_max=0

    for n in reversed(arr):

        max_right[i]=max(n, prev_max)
        prev_max= max_right[i]
        i-=1


    l=0
    res=0

    for r in range(len(arr)):

        while arr[l]> max_right[r]:
            l+=1

        res= max(res, r-l)        

    return res    