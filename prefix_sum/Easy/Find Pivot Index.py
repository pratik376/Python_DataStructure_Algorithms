def pivotIndex(arr):

    left=arr[0]
    right=sum(arr)

    if (left==right):
        return 0
    
    for i in range(1, len(arr)):

        left+=arr[i]
        right-=arr[i-1]

        if (left==right): 
            return i

    return -1    


def pivotIndex(arr):

    left=0
    right= sum(arr)

    for i in range(len(arr)):

        righ-=arr[i]

        if left== right:
            return i
        
        left+=arr[i]
    return -1    