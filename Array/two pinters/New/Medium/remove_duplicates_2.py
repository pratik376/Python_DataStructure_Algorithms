
def removeDuplicates(arr):

    l,r=0,0

    while r < len(arr):
        count=1

        while r+1< len(arr) and arr[r]==arr[r+1]:
            r+=1
            count+=1

        for i in range(min(2,count)):

            arr[l]=arr[r]
            l+=1

        r+=1
    return l      