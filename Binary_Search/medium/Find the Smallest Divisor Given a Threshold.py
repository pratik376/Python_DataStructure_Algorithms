import math
def findtheSmallestDivisor(arr,threshold):

    l,r= 1, max(arr)
    answer=float('inf')

    while l<=r:

        mid = (l+r)//2

        my_sum=0
        for data in arr:
            my_sum+= math.ceil(data/mid)

        if my_sum >  threshold:
            l=mid+1
        else:
            r=mid-1
            answer= min(answer, mid)


    #    if my_sum >  threshold:
    #       l=mid+1
    #    else 
    #     r= mid-1
    # return l --> think about this

    # */     

    return answer        



            