def splitarray(arr,m):

    l, r = max(arr), sum(arr)
    res=r

    def isSplit(mid):

        sub_array=0
        curSum=0

        for val in arr:
            curSum+=val

            if curSum>mid:
                sub_array+=1
                curSum=val

        return sub_array+1 <= m        

    while l <=r:

        mid= (l+r)//2

        if isSplit(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1
    return res        

