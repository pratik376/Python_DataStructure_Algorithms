def singleSortedArray(arr):

    l, r = 0, len(arr) - 1

    while l <= r:

        m = (l + r) // 2

        if (m - 1 < 0 or arr[m - 1] != arr[m]) and (
            m + 1 == len(arr) or arr[m] != arr[m + 1]
        ):
            return arr[m]
        
        leftSize= m-1 if arr[m]== arr[m-1] else m # we counting element

        if leftSize % 2 :
            r=m-1
        else:
            l=m+1    

