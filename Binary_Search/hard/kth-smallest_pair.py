import math
def smallestPair(arr,k):


    def slidingWindowCount(arr,mid):
        i=0
        j=1
        pairCount=0

        while j< len(arr):

            while i<j and abs(arr[j] -arr[i]) > mid:
                i+=1

            pairCount+=(j-i)
            j+=1    
        
        return pairCount




    n=len(arr)
    arr.sort()

    l, r= 0, arr[-1] - arr[0]


    result=0

    while l<=r:

        mid= (l+r)//2

        countPair=slidingWindowCount(arr,mid)

        if countPair < k:
            l=mid+1
        else:
            result=mid
            r=mid-1

    return result    


# other method





def smallestPair(arr,k):

    n= len(arr)
    max_element= max(arr)- min(arr)
    vec=[0] * (max_element+1)

    for i in range(n):
        for j in range(i+1,n):

            diff= abs(arr[i]- arr[j])

            vec[diff]+=1

    for i in range(len(vec)):

        k-=vec[i]

        if k<=0:
            return i

    return -1    


