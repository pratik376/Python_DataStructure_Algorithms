def findPeaks(arr):

    pics=[]

    n= len(arr)


    for i in range(1, n-1):

        if arr[i]> arr[i-1] and arr[i]> arr[i+1]:
            pics.append(i)
    return pics                   