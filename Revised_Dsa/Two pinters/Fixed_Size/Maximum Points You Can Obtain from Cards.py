# Practice this again


def maximumPoints(arr,k):
    l,r= 0, len(arr)-k

    total=sum(arr[r:])
    res=total

    while r< len(arr):

        total += (arr[l]- arr[r])
        res=max(res,total)
        i+=1
        r+=1
    return res     


